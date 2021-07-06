
from pathlib import Path
import tinydb
import datetime
from tinydb.middlewares import CachingMiddleware
from tinydb.storages import JSONStorage


class LogsDb(tinydb.TinyDB):
    '''
    A database to storage build log
    Item
    {
        "exit-code": 0,
        "user-time": 0.46,
        "system-time": 0.28,
        "time": 3.74,
        "subdir": "package/utils/e2fsprogs",
        "target": "",
        "build-type": "",
        "build-variant": "compile",
        "detail" : "",
        'arch': 'x86',
        'board': '64',
        'run-number': 123,
        'issue-id': 13432,
        'banned': False,
    }
    '''

    def __init__(self, db_dir: Path):
        db_path = db_dir.joinpath('logs.db.json')
        self.db_dir = db_dir
        super().__init__(db_path,
                         storage=CachingMiddleware(JSONStorage),
                         indent=2, separators=(',', ': '))

    @classmethod
    def query(cls, **kwargs):
        'generate common Query instance'
        Item = tinydb.Query()
        ans = ((Item.subdir == kwargs['subdir']) &
               (Item.target == kwargs['target']) &
               (Item['build-type'] == kwargs['build-type']) &
               (Item['build-variant'] == kwargs['build-variant']) &
               (Item.arch == kwargs['arch']) &
               (Item.board == kwargs['board']))
        # run_id = kwargs.pop('run-number', 0)
        # if run_id != 0:
        #     ans = (ans & (Item['run-number'] == run_id))
        return ans

    @classmethod
    def merge(cls, logAst: object, arch: str, board: str = None, run_number: int = 0):
        'merge everything together'
        ans = {}
        ans.update(logAst)
        ans['arch'] = arch
        ans['board'] = board
        ans['run-number'] = run_number
        return ans

    @classmethod
    def cost_func(cls, docs: list):
        'a function to caculate cost'
        cost = 0
        l = len(docs)
        for i in range(l):
            if docs[i]['exit-code'] != 0:
                continue
            #
            # lim(i=1,+\infinty) 1/1 + 1/2 + ... + 1/i < 2
            #
            # cost += docs[i]['time'] / (l - i)
            cost += docs[i]['time']  # not enought data now
        return cost

    def count_errors(self, arch: str, board: str = None, run_number: int = 0):
        'count errors'
        Item = tinydb.Query()
        return len(self.search(
            (Item['run-number'] == run_number) &
            (Item.arch == arch) &
            (Item.board == board) &
            (Item['exit-code'] != 0))
        )

    def compress(self):
        'bundle some items which has same arch and board together to reduce database file'
        Item = tinydb.Query()
        groups = {}
        removedIDs = []
        # clean exit-code != 0
        # for doc in self.search(Item['exit-code'] != 0):
        #     removedIDs.append(doc.doc_id)
        #     pass
        for doc in self.search(Item['exit-code'] == 0):
            removedIDs.append(doc.doc_id)
            idGroup = [doc['arch'], doc['board'], doc['subdir'],
                       doc['target'], doc['build-type'], doc['build-variant']]
            idGroup = str(idGroup)
            if groups.get(idGroup) == None:
                groups[idGroup] = dict(doc)
                groups[idGroup]['count'] = 1
                groups[idGroup]['run-number'] = 0
                groups[idGroup]['detail'] = None
                pass
            else:
                groups[idGroup]['count'] += 1
                groups[idGroup]['user-time'] += doc['user-time']
                groups[idGroup]['system-time'] += doc['system-time']
                groups[idGroup]['time'] += doc['time']
                pass
            pass
        self.remove(doc_ids=removedIDs)
        for key, val in groups.items():
            val['user-time'] /= val['count']
            val['system-time'] /= val['count']
            val['time'] /= val['count']
            del val['count']
            pass
        self.insert_multiple(groups[key] for key in groups)
        pass

    def transform_and_exit(self, compress: bool = False):
        'transform to hugo contents and close database for reducing db size'
        Item = tinydb.Query()
        for doc in self.search(Item['exit-code'] != 0):
            if doc['detail'] is None:  # avoid to override exist hugo content
                continue
            # create hugo md file path
            hugo_dir_list = []
            for key in ['arch', 'board', 'subdir', 'target']:
                val: str = doc[key]
                if val == "":
                    continue
                hugo_dir_list.append(val.replace('/', '_'))
            # print(hugo_dir_list)
            hugo_dir = self.db_dir.joinpath('content')
            # TODO: dry run mode
            hugo_dir.mkdir(parents=True, exist_ok=True)
            for idx, val in enumerate(hugo_dir_list):
                val: str = val
                hugo_dir = hugo_dir.joinpath(val)
                # TODO: dry run mode
                hugo_dir.mkdir(parents=True, exist_ok=True)
                hugo_dir.joinpath('_index.md').write_text('''---
title: "%s"
date: %s
hidden: false
draft: false
---

%s

''' % (val, datetime.datetime.now(), '/'.join(hugo_dir_list[:idx+1]))
                )
                # print(hugo_dir, hugo_dir_list[:idx+1], val)

            # create markdown file name
            md_name = (doc['build-type'] +
                       '-') if doc['build-type'] != '' else ''
            md_name += '%s.%s.md' % (doc['build-variant'], doc['run-number'])
            # print(md_name)
            hugo_dir.joinpath(md_name).write_text(
                self._build_hugo_content(doc))

        self.update({'detail': None})
        if(compress):
            self.compress()
        self.close()

    def _build_hugo_content(self, doc) -> str:
        ans = '''---
title: "%s.%s"
date: %s
hidden: false
draft: false
weight: -%s
---
''' % (((doc['build-type'] + '-') if doc['build-type'] != '' else '') + doc['build-variant'], doc['run-number'],
            datetime.datetime.now(),
            doc['run-number']
       )
        build_cmd = doc['subdir'] + '/' + ((doc['build-type'] + '-') if doc['build-type']
                                           != '' else '') + doc['build-variant']

        ans += '''
build number: `%s`

#### re-implement command 

```bash
docker pull immortalwrt/opde:sdk
docker run -it --rm immortalwrt/opde:sdk zsh # or bash
export http_proxy= # [your proxy], do not use localhost or 127.0.0.1
export https_proxy=$http_proxy
opde feeds && opde config -a
make %s -j$(nproc) || make %s V=s
```

#### Compile.txt

``` bash
%s
```
''' % (doc['run-number'], build_cmd, build_cmd, doc['detail'])
        return ans
