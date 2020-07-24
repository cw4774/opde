import networkx as nx
import json
import sys
from pathlib import Path


class DependsTree():
    '''
    Packages dependence tree
    build from targetinfo and packageinfo ast
    '''

    _default_cost = 1

    def __init__(self):
        self.dg = nx.DiGraph()

    def draw(self):
        'draw dag, very slow, not recommand'
        import matplotlib.pyplot as plt
        plt.subplot(111)
        nx.draw_shell(self.dg, with_labels=True, font_weight='normal',
                      font_size=10, node_color="#F4D03F")

    def inject_package_info(self, packageInfoAst):
        '''
        build depends graph from packageinfo ast, this is dag
        '''
        def debugger(cond: bool, *args, **kwargs):
            if cond:
                from pprint import pprint
                pprint(kwargs)
                raise BaseException('debug')
        for makefile in packageInfoAst:
            for pack in makefile['packages']:
                self.dg.add_node(pack['Package'], pack=pack,
                                 makefile=makefile, type=pack['Type'], cost=0)
                if 'Provides' in pack and pack['Provides'].count(' ') != 0:
                    print(pack['Provides'])
                for dep in pack['Depends']:
                    # TODO: more depends
                    if dep[0] == 'DEPENDS_SELECT_OTH' or dep[0] == 'DEPENDS_WAIT_OTH_SELECTED':
                        self.dg.add_node(dep[1], cost=0, type='unknown')
                        self.dg.add_edge(pack['Package'], dep[1])
                    # if dep[0] == 'DEPENDS_SELECT_OTH_IF': # TODO: check condiction
                    #     self.dg.add_node(dep[2])
                    #     self.dg.add_edge(pack['Package'],dep[2])
        # some packages in same makefile are build in the same time, just like: golang, golang-doc, golang-src
        # let's make a virtual package to bundle together
        # TODO: consider condiction
        for makefile in packageInfoAst:
            source = Path(makefile['Source-Makefile']).parent.as_posix()
            self.dg.add_node(source, type='source',
                             cost=self._default_cost, makefile=makefile)
            variants = set()
            packs = set()
            for pack in makefile['packages']:
                packs.add(pack['Package'])
                if 'Build-Variant' in pack and pack['Build-Variant'] != '':
                    variant = Path(source).joinpath(
                        pack['Build-Variant']).as_posix()
                    variants.add(variant)
                    self.dg.add_node(variant, makefile=makefile,
                                     type='variant', cost=self._default_cost)
                    # self.dg.nodes[source]['cost'] = 0
                    self.dg.add_edge(variant, pack['Package'])
                    self.dg.add_node(pack['Package'], owner=variant)
                else:
                    self.dg.add_edge(source, pack['Package'])
                    self.dg.add_node(pack['Package'], owner=source)
                # if 'Build-Variant' not in pack and pack['Provides'] != '':
                    # print(pack['Package'])
            # debug only
            # n1 = 'pulseaudio'
            # n2 = 'package/feeds/packages/pulseaudio/noavahi'
            # n2 = n1 = ''
            # debugger(self.dg.has_edge(n1, n2),pos=1)
            # source depends on variants
            for variant in variants:
                self.dg.add_edge(source, variant)
            # debugger(self.dg.has_edge(n1, n2),pos=2)
            for pack in makefile['packages']:
                for edge in self.dg.in_edges(pack['Package']):
                    # avoid to create cycle path
                    if (edge[0] == source) or (edge[0] in variants) or (edge[0] in packs):
                        continue
                    if 'Build-Variant' in pack and pack['Build-Variant'] != '':
                        variant = Path(source).joinpath(
                            pack['Build-Variant']).as_posix()
                        if self.dg.has_edge(variant, edge[0]):
                            continue
                        self.dg.add_edge(edge[0], variant)
                        # debugger(self.dg.has_edge(n1, n2),pos=3, source=source,
                        #     edge=edge, variant=variant, variants=variants,
                        #     inedges=self.dg.in_edges(pack['Package']))
                    else:
                        if self.dg.has_edge(source, edge[0]):
                            continue
                        self.dg.add_edge(edge[0], source)
                        # debugger(self.dg.has_edge(n1, n2),pos=4)
            # debugger(self.dg.has_edge(n1, n2),pos=5)
        # debug only
        # (n1, n2) = ( 'package/feeds/packages/pulseaudio/noavahi', 'pulseaudio-tools')
        # (n1, n2) = ('', '')
        # debugger(self.dg.has_edge(n1, n2),pos=0)
        for makefile in packageInfoAst:
            for pack in makefile['packages']:
                for i in pack['Provides']:
                    if isinstance(i, str):
                        pyd = i
                    elif isinstance(i, list):
                        pyd = i[0]  # FIXME: ignore version compare
                    else:
                        raise BaseException('unexpect type')
                    if pyd == pack['Package']:
                        continue
                    if not self.dg.has_node(pyd) or self.dg.nodes[pyd]['type'] == 'provider':
                        self.dg.add_node(pyd, type='provider',
                                         cost=self._default_cost)
                        self.dg.add_edge(
                            pyd, self.dg.nodes[pack['Package']]['owner'])
                        # debugger(self.dg.has_edge(n1, n2),pos=6)
                    elif self.dg.nodes[pyd]['type'] == 'unknown':
                        if pyd == self.dg.nodes[pack['Package']]['owner']:
                            continue
                        self.dg.add_node(pyd, type='provider', cost=0)
                        self.dg.add_edge(
                            pyd, self.dg.nodes[pack['Package']]['owner'])
                        # debugger(self.dg.has_edge(n1, n2),pos=7, frm=pyd,
                        #     to=self.dg.nodes[pack['Package']]['owner'])
                    elif self.dg.nodes[pyd]['type'] == 'variant' or self.dg.nodes[pyd]['type'] == 'source':
                        raise BaseException('Impossible!')
                    else:  # type is normal ipkg, bin
                        # print(pyd, self.dg.nodes[pyd].keys())
                        # pyd_before = pyd
                        pyd = self.dg.nodes[pyd]['owner']  # switch to owner
                        if pyd == self.dg.nodes[pack['Package']]['owner']:
                            continue
                        self.dg.add_edge(
                            pyd, self.dg.nodes[pack['Package']]['owner'])
                        # debugger(self.dg.has_edge(n1, n2),pos=8,before=pyd_before, pyd=pyd,
                        #     to=self.dg.nodes[pack['Package']]['owner'])
        # shrink some cycles to a singular node
        cycles = [
            ['package/kernel/ath10k-ct/regular',
                'kmod-ath10k-ct', 'package/kernel/mac80211'],
            ['package/kernel/mac80211', 'package/kernel/ath10k-ct/smallbuffers',
                'kmod-ath10k-ct-smallbuffers'],
            ['package/feeds/packages/pulseaudio/noavahi',
                'pulseaudio-tools', 'pulseaudio'],
            ['kmod-openvswitch', 'package/feeds/packages/openvswitch'],
        ]
        for cycle in cycles:
            name = str(cycle)
            for node in cycle:
                for in_edge in self.dg.in_edges(node):
                    self.dg.add_edge(in_edge[0], name)
            self.dg.remove_edges_from(
                [(cycle[i], cycle[(i + 1) % len(cycle)]) for i in range(len(cycle))])
            self.dg.add_node(name, type='shrink', cost=0)
        # pprint(dep)
        # print(self.dg.nodes().data())
        idx = 0
        for node in self.dg.nodes():
            # record index in each node for reverse-quering
            self.dg.add_node(node, numid=idx)
            idx += 1
        # print(self.dg['base-files'])
        if not nx.is_directed_acyclic_graph(self.dg):
            print('Ring detect! This is not DAG!!', file=sys.stderr)
            print(nx.find_cycle(self.dg))

    def inject_costs(self, logsAST: object):
        '''
        inject cost from logs
        '''
        for log in logsAST:
            if log['exit-code'] != 0:  # build has some error
                continue
            pkg_name = log['subdir']
            if log['target'] != '':
                pkg_name = '/'.join([pkg_name, log['target']])
            if not self.dg.has_node(pkg_name):
                print("%s package isn't registed in DependsTree, skip..." % pkg_name)
                continue
            # TODO: confuse about user-time system-time and time
            self.dg.nodes[pkg_name]['cost'] = log['time']
            # print(log)
            # break

    def to_json(self):
        '''
        output json to represent dag
        '''
        ans = {
            'nodes': [],
            'edges': []
        }
        for node in self.dg.nodes():
            data = self.dg.nodes[node]
            ans['nodes'].append(
                {'name': node, 'cost': data['cost'], 'id': data['numid']})
        for edge in self.dg.edges():
            ans['edges'].append(
                {'from': self.dg.nodes[edge[0]]['numid'], 'to': self.dg.nodes[edge[1]]['numid']})
        return json.dumps(ans, indent=2)
