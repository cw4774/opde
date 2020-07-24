
# packageParseTab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rootCONFIG CONFIG_HELP CONFIG_HELP_END CONFIG_HELP_LINE CONFIG_ITEM DELIMITER DEPENDS DEPENDS_END DEPENDS_SELECT_OTH DEPENDS_SELECT_OTH_IF DEPENDS_SELECT_SYMBOL DEPENDS_WAIT_OTH_SELECTED DEPENDS_WAIT_OTH_SELECTED_IF DEPENDS_WAIT_SYMBOL DERIVATE DESCRIPTION PACKAGEID PARAMS PROVIDES PROVIDES_END PROVIDES_ITEM SOURCE\n        root : source\n             | root source\n        packs : pack\n              | packs pack\n        depsext : depend\n             | depsext depend\n        confx : configItem\n              | confx configItem\n        helpx : CONFIG_HELP_LINE\n              | helpx CONFIG_HELP_LINE\n        providx : PROVIDES_ITEM\n              | providx PROVIDES_ITEM\n        \n        deps   : depsext DEPENDS_END\n        helpdoc : helpx CONFIG_HELP_END\n        provides : providx PROVIDES_END\n        \n        deps : DEPENDS_END\n        helpdoc : CONFIG_HELP_END\n        provides : PROVIDES_END\n        \n        properties : kv\n                    | properties kv\n        sourceComb : sourceid properties\n                   | sourceid\n        packageComb : packageid properties\n                    | packageid properties configComb\n        \n        kv : DERIVATE PARAMS\n           | DESCRIPTION PARAMS DELIMITER\n           | PROVIDES provides\n           | DEPENDS deps\n        sourceid : SOURCE PARAMS\n        packageid : PACKAGEID PARAMS\n        configComb : CONFIG confx DELIMITER\n        configItem : CONFIG_ITEM PARAMS\n                   | CONFIG_HELP helpdoc\n        \n        source : sourceComb packs\n        \n        pack : packageComb\n        \n        depend : DEPENDS_SELECT_OTH\n               | DEPENDS_SELECT_OTH_IF\n               | DEPENDS_WAIT_SYMBOL\n               | DEPENDS_WAIT_OTH_SELECTED\n               | DEPENDS_WAIT_OTH_SELECTED_IF\n               | DEPENDS_SELECT_SYMBOL\n        '
    
_lr_action_items = {'SOURCE':([0,1,2,6,7,8,9,13,19,20,22,23,25,27,29,31,39,41,42,44,50,],[5,5,-1,-2,-34,-3,-35,-19,-4,-23,-20,-25,-27,-18,-28,-16,-24,-26,-15,-13,-31,]),'$end':([1,2,6,7,8,9,13,19,20,22,23,25,27,29,31,39,41,42,44,50,],[0,-1,-2,-34,-3,-35,-19,-4,-23,-20,-25,-27,-18,-28,-16,-24,-26,-15,-13,-31,]),'PACKAGEID':([3,4,7,8,9,12,13,18,19,20,22,23,25,27,29,31,39,41,42,44,50,],[11,-22,11,-3,-35,-21,-19,-29,-4,-23,-20,-25,-27,-18,-28,-16,-24,-26,-15,-13,-31,]),'DERIVATE':([4,10,12,13,18,20,21,22,23,25,27,29,31,41,42,44,],[14,14,14,-19,-29,14,-30,-20,-25,-27,-18,-28,-16,-26,-15,-13,]),'DESCRIPTION':([4,10,12,13,18,20,21,22,23,25,27,29,31,41,42,44,],[15,15,15,-19,-29,15,-30,-20,-25,-27,-18,-28,-16,-26,-15,-13,]),'PROVIDES':([4,10,12,13,18,20,21,22,23,25,27,29,31,41,42,44,],[16,16,16,-19,-29,16,-30,-20,-25,-27,-18,-28,-16,-26,-15,-13,]),'DEPENDS':([4,10,12,13,18,20,21,22,23,25,27,29,31,41,42,44,],[17,17,17,-19,-29,17,-30,-20,-25,-27,-18,-28,-16,-26,-15,-13,]),'PARAMS':([5,11,14,15,48,],[18,21,23,24,52,]),'CONFIG':([13,20,22,23,25,27,29,31,41,42,44,],[-19,40,-20,-25,-27,-18,-28,-16,-26,-15,-13,]),'PROVIDES_END':([16,26,28,43,],[27,42,-11,-12,]),'PROVIDES_ITEM':([16,26,28,43,],[28,43,-11,-12,]),'DEPENDS_END':([17,30,32,33,34,35,36,37,38,45,],[31,44,-5,-36,-37,-38,-39,-40,-41,-6,]),'DEPENDS_SELECT_OTH':([17,30,32,33,34,35,36,37,38,45,],[33,33,-5,-36,-37,-38,-39,-40,-41,-6,]),'DEPENDS_SELECT_OTH_IF':([17,30,32,33,34,35,36,37,38,45,],[34,34,-5,-36,-37,-38,-39,-40,-41,-6,]),'DEPENDS_WAIT_SYMBOL':([17,30,32,33,34,35,36,37,38,45,],[35,35,-5,-36,-37,-38,-39,-40,-41,-6,]),'DEPENDS_WAIT_OTH_SELECTED':([17,30,32,33,34,35,36,37,38,45,],[36,36,-5,-36,-37,-38,-39,-40,-41,-6,]),'DEPENDS_WAIT_OTH_SELECTED_IF':([17,30,32,33,34,35,36,37,38,45,],[37,37,-5,-36,-37,-38,-39,-40,-41,-6,]),'DEPENDS_SELECT_SYMBOL':([17,30,32,33,34,35,36,37,38,45,],[38,38,-5,-36,-37,-38,-39,-40,-41,-6,]),'DELIMITER':([24,46,47,51,52,53,55,57,],[41,50,-7,-8,-32,-33,-17,-14,]),'CONFIG_ITEM':([40,46,47,51,52,53,55,57,],[48,48,-7,-8,-32,-33,-17,-14,]),'CONFIG_HELP':([40,46,47,51,52,53,55,57,],[49,49,-7,-8,-32,-33,-17,-14,]),'CONFIG_HELP_END':([49,54,56,58,],[55,57,-9,-10,]),'CONFIG_HELP_LINE':([49,54,56,58,],[56,58,-9,-10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'root':([0,],[1,]),'source':([0,1,],[2,6,]),'sourceComb':([0,1,],[3,3,]),'sourceid':([0,1,],[4,4,]),'packs':([3,],[7,]),'pack':([3,7,],[8,19,]),'packageComb':([3,7,],[9,9,]),'packageid':([3,7,],[10,10,]),'properties':([4,10,],[12,20,]),'kv':([4,10,12,20,],[13,13,22,22,]),'provides':([16,],[25,]),'providx':([16,],[26,]),'deps':([17,],[29,]),'depsext':([17,],[30,]),'depend':([17,30,],[32,45,]),'configComb':([20,],[39,]),'confx':([40,],[46,]),'configItem':([40,46,],[47,51,]),'helpdoc':([49,],[53,]),'helpx':([49,],[54,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> root","S'",1,None,None,None),
  ('root -> source','root',1,'p_list_init','packageinfo.py',27),
  ('root -> root source','root',2,'p_list_init','packageinfo.py',28),
  ('packs -> pack','packs',1,'p_list_init','packageinfo.py',29),
  ('packs -> packs pack','packs',2,'p_list_init','packageinfo.py',30),
  ('depsext -> depend','depsext',1,'p_list_init','packageinfo.py',31),
  ('depsext -> depsext depend','depsext',2,'p_list_init','packageinfo.py',32),
  ('confx -> configItem','confx',1,'p_list_init','packageinfo.py',33),
  ('confx -> confx configItem','confx',2,'p_list_init','packageinfo.py',34),
  ('helpx -> CONFIG_HELP_LINE','helpx',1,'p_list_init','packageinfo.py',35),
  ('helpx -> helpx CONFIG_HELP_LINE','helpx',2,'p_list_init','packageinfo.py',36),
  ('providx -> PROVIDES_ITEM','providx',1,'p_list_init','packageinfo.py',37),
  ('providx -> providx PROVIDES_ITEM','providx',2,'p_list_init','packageinfo.py',38),
  ('deps -> depsext DEPENDS_END','deps',2,'p_list_end','packageinfo.py',47),
  ('helpdoc -> helpx CONFIG_HELP_END','helpdoc',2,'p_list_end','packageinfo.py',48),
  ('provides -> providx PROVIDES_END','provides',2,'p_list_end','packageinfo.py',49),
  ('deps -> DEPENDS_END','deps',1,'p_list_singular','packageinfo.py',55),
  ('helpdoc -> CONFIG_HELP_END','helpdoc',1,'p_list_singular','packageinfo.py',56),
  ('provides -> PROVIDES_END','provides',1,'p_list_singular','packageinfo.py',57),
  ('properties -> kv','properties',1,'p_bundle','packageinfo.py',63),
  ('properties -> properties kv','properties',2,'p_bundle','packageinfo.py',64),
  ('sourceComb -> sourceid properties','sourceComb',2,'p_bundle','packageinfo.py',65),
  ('sourceComb -> sourceid','sourceComb',1,'p_bundle','packageinfo.py',66),
  ('packageComb -> packageid properties','packageComb',2,'p_bundle','packageinfo.py',67),
  ('packageComb -> packageid properties configComb','packageComb',3,'p_bundle','packageinfo.py',68),
  ('kv -> DERIVATE PARAMS','kv',2,'p_kv','packageinfo.py',78),
  ('kv -> DESCRIPTION PARAMS DELIMITER','kv',3,'p_kv','packageinfo.py',79),
  ('kv -> PROVIDES provides','kv',2,'p_kv','packageinfo.py',80),
  ('kv -> DEPENDS deps','kv',2,'p_kv','packageinfo.py',81),
  ('sourceid -> SOURCE PARAMS','sourceid',2,'p_kv','packageinfo.py',82),
  ('packageid -> PACKAGEID PARAMS','packageid',2,'p_kv','packageinfo.py',83),
  ('configComb -> CONFIG confx DELIMITER','configComb',3,'p_kv','packageinfo.py',84),
  ('configItem -> CONFIG_ITEM PARAMS','configItem',2,'p_kv','packageinfo.py',85),
  ('configItem -> CONFIG_HELP helpdoc','configItem',2,'p_kv','packageinfo.py',86),
  ('source -> sourceComb packs','source',2,'p_source','packageinfo.py',94),
  ('pack -> packageComb','pack',1,'p_pack','packageinfo.py',102),
  ('depend -> DEPENDS_SELECT_OTH','depend',1,'p_depend','packageinfo.py',110),
  ('depend -> DEPENDS_SELECT_OTH_IF','depend',1,'p_depend','packageinfo.py',111),
  ('depend -> DEPENDS_WAIT_SYMBOL','depend',1,'p_depend','packageinfo.py',112),
  ('depend -> DEPENDS_WAIT_OTH_SELECTED','depend',1,'p_depend','packageinfo.py',113),
  ('depend -> DEPENDS_WAIT_OTH_SELECTED_IF','depend',1,'p_depend','packageinfo.py',114),
  ('depend -> DEPENDS_SELECT_SYMBOL','depend',1,'p_depend','packageinfo.py',115),
]
