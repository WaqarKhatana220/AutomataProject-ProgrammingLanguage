
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'SleftLPARENRPARENAND BOOL CHAR COMMA DIVIDE ELIF ELSE EQUAL EQUALEQUAL FLOAT GREATERTHAN GREATERTHANEQUALTO IF INT LCBRACKET LESSTHAN LESSTHANEQUALTO LPAREN MINUS MINUSMINUS MODULUS MULTIPLY NAME NOT NOTEQUAL OR PLUS PLUSPLUS POWER PRINT RCBRACKET RPAREN SEMICOLON STRING bool char float int string\n    S : stmt S\n    \n    stmt : NAME operator SEMICOLON\n    \n    operator : PLUSPLUS\n            | MINUSMINUS\n    \n    S :\n    \n    stmt : IF LPAREN exp RPAREN LCBRACKET stmt RCBRACKET\n    \n    stmt : ELIF LPAREN exp RPAREN LCBRACKET stmt RCBRACKET\n    \n    stmt : ELSE LCBRACKET stmt RCBRACKET\n    \n    stmt : PRINT LPAREN exp RPAREN SEMICOLON\n     \n    exp : exp PLUS exp\n        | exp MINUS exp\n        | exp DIVIDE exp\n        | exp MULTIPLY exp\n        | exp MODULUS exp\n        | exp POWER exp\n        | exp LESSTHAN exp\n        | exp GREATERTHAN exp\n        | exp GREATERTHANEQUALTO exp\n        | exp LESSTHANEQUALTO exp\n        | exp NOTEQUAL exp\n        | exp EQUALEQUAL exp\n        | exp AND exp\n        | exp OR exp\n    \n    exp : LPAREN exp RPAREN\n     \n    exp : exp COMMA exp\n    \n    exp : INT\n        | FLOAT\n    \n    exp : STRING\n    \n    exp : CHAR\n    \n    exp : BOOL\n    \n    exp : NAME\n    \n    stmt : DTYPE NAME EQUAL exp SEMICOLON\n    \n    DTYPE : int\n        | string\n        | float\n        | bool\n        | char\n    \n    stmt : NAME EQUAL exp SEMICOLON\n    '
    
_lr_action_items = {'$end':([0,1,2,14,24,38,57,78,79,82,83,],[-5,0,-5,-1,-2,-38,-8,-9,-32,-6,-7,]),'NAME':([0,2,8,9,10,11,12,13,16,19,20,21,22,24,27,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,57,76,77,78,79,82,83,],[3,3,23,-33,-34,-35,-36,-37,25,25,25,3,25,-2,25,25,-38,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,-8,3,3,-9,-32,-6,-7,]),'IF':([0,2,21,24,38,57,76,77,78,79,82,83,],[4,4,4,-2,-38,-8,4,4,-9,-32,-6,-7,]),'ELIF':([0,2,21,24,38,57,76,77,78,79,82,83,],[5,5,5,-2,-38,-8,5,5,-9,-32,-6,-7,]),'ELSE':([0,2,21,24,38,57,76,77,78,79,82,83,],[6,6,6,-2,-38,-8,6,6,-9,-32,-6,-7,]),'PRINT':([0,2,21,24,38,57,76,77,78,79,82,83,],[7,7,7,-2,-38,-8,7,7,-9,-32,-6,-7,]),'int':([0,2,21,24,38,57,76,77,78,79,82,83,],[9,9,9,-2,-38,-8,9,9,-9,-32,-6,-7,]),'string':([0,2,21,24,38,57,76,77,78,79,82,83,],[10,10,10,-2,-38,-8,10,10,-9,-32,-6,-7,]),'float':([0,2,21,24,38,57,76,77,78,79,82,83,],[11,11,11,-2,-38,-8,11,11,-9,-32,-6,-7,]),'bool':([0,2,21,24,38,57,76,77,78,79,82,83,],[12,12,12,-2,-38,-8,12,12,-9,-32,-6,-7,]),'char':([0,2,21,24,38,57,76,77,78,79,82,83,],[13,13,13,-2,-38,-8,13,13,-9,-32,-6,-7,]),'EQUAL':([3,23,],[16,37,]),'PLUSPLUS':([3,],[17,]),'MINUSMINUS':([3,],[18,]),'LPAREN':([4,5,7,16,19,20,22,27,37,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[19,20,22,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'LCBRACKET':([6,55,56,],[21,76,77,]),'SEMICOLON':([15,17,18,25,26,28,29,30,31,32,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,],[24,-3,-4,-31,38,-26,-27,-28,-29,-30,78,79,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-25,-24,]),'INT':([16,19,20,22,27,37,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,28,]),'FLOAT':([16,19,20,22,27,37,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'STRING':([16,19,20,22,27,37,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'CHAR':([16,19,20,22,27,37,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,]),'BOOL':([16,19,20,22,27,37,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'RCBRACKET':([24,35,38,57,78,79,80,81,82,83,],[-2,57,-38,-8,-9,-32,82,83,-6,-7,]),'PLUS':([25,26,28,29,30,31,32,33,34,36,54,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,],[-31,39,-26,-27,-28,-29,-30,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,39,-24,]),'MINUS':([25,26,28,29,30,31,32,33,34,36,54,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,],[-31,40,-26,-27,-28,-29,-30,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,-24,]),'DIVIDE':([25,26,28,29,30,31,32,33,34,36,54,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,],[-31,41,-26,-27,-28,-29,-30,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,41,-24,]),'MULTIPLY':([25,26,28,29,30,31,32,33,34,36,54,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,],[-31,42,-26,-27,-28,-29,-30,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,-24,]),'MODULUS':([25,26,28,29,30,31,32,33,34,36,54,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,],[-31,43,-26,-27,-28,-29,-30,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,-24,]),'POWER':([25,26,28,29,30,31,32,33,34,36,54,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,],[-31,44,-26,-27,-28,-29,-30,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,-24,]),'LESSTHAN':([25,26,28,29,30,31,32,33,34,36,54,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,],[-31,45,-26,-27,-28,-29,-30,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-24,]),'GREATERTHAN':([25,26,28,29,30,31,32,33,34,36,54,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,],[-31,46,-26,-27,-28,-29,-30,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,-24,]),'GREATERTHANEQUALTO':([25,26,28,29,30,31,32,33,34,36,54,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,],[-31,47,-26,-27,-28,-29,-30,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,-24,]),'LESSTHANEQUALTO':([25,26,28,29,30,31,32,33,34,36,54,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,],[-31,48,-26,-27,-28,-29,-30,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,-24,]),'NOTEQUAL':([25,26,28,29,30,31,32,33,34,36,54,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,],[-31,49,-26,-27,-28,-29,-30,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,-24,]),'EQUALEQUAL':([25,26,28,29,30,31,32,33,34,36,54,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,],[-31,50,-26,-27,-28,-29,-30,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,-24,]),'AND':([25,26,28,29,30,31,32,33,34,36,54,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,],[-31,51,-26,-27,-28,-29,-30,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,-24,]),'OR':([25,26,28,29,30,31,32,33,34,36,54,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,],[-31,52,-26,-27,-28,-29,-30,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,-24,]),'COMMA':([25,26,28,29,30,31,32,33,34,36,54,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,],[-31,53,-26,-27,-28,-29,-30,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,-24,]),'RPAREN':([25,28,29,30,31,32,33,34,36,54,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,],[-31,-26,-27,-28,-29,-30,55,56,58,75,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-25,-24,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'S':([0,2,],[1,14,]),'stmt':([0,2,21,76,77,],[2,2,35,80,81,]),'DTYPE':([0,2,21,76,77,],[8,8,8,8,8,]),'operator':([3,],[15,]),'exp':([16,19,20,22,27,37,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,],[26,33,34,36,54,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> S","S'",1,None,None,None),
  ('S -> stmt S','S',2,'p_start','yapl_parser.py',28),
  ('stmt -> NAME operator SEMICOLON','stmt',3,'p_inc_dec_rement','yapl_parser.py',35),
  ('operator -> PLUSPLUS','operator',1,'p_operator','yapl_parser.py',41),
  ('operator -> MINUSMINUS','operator',1,'p_operator','yapl_parser.py',42),
  ('S -> <empty>','S',0,'p_start_empty','yapl_parser.py',48),
  ('stmt -> IF LPAREN exp RPAREN LCBRACKET stmt RCBRACKET','stmt',7,'p_conditional_if','yapl_parser.py',55),
  ('stmt -> ELIF LPAREN exp RPAREN LCBRACKET stmt RCBRACKET','stmt',7,'p_conditional_elif','yapl_parser.py',61),
  ('stmt -> ELSE LCBRACKET stmt RCBRACKET','stmt',4,'p_conditional_else','yapl_parser.py',67),
  ('stmt -> PRINT LPAREN exp RPAREN SEMICOLON','stmt',5,'p_print_stmt','yapl_parser.py',74),
  ('exp -> exp PLUS exp','exp',3,'p_exp_bin','yapl_parser.py',80),
  ('exp -> exp MINUS exp','exp',3,'p_exp_bin','yapl_parser.py',81),
  ('exp -> exp DIVIDE exp','exp',3,'p_exp_bin','yapl_parser.py',82),
  ('exp -> exp MULTIPLY exp','exp',3,'p_exp_bin','yapl_parser.py',83),
  ('exp -> exp MODULUS exp','exp',3,'p_exp_bin','yapl_parser.py',84),
  ('exp -> exp POWER exp','exp',3,'p_exp_bin','yapl_parser.py',85),
  ('exp -> exp LESSTHAN exp','exp',3,'p_exp_bin','yapl_parser.py',86),
  ('exp -> exp GREATERTHAN exp','exp',3,'p_exp_bin','yapl_parser.py',87),
  ('exp -> exp GREATERTHANEQUALTO exp','exp',3,'p_exp_bin','yapl_parser.py',88),
  ('exp -> exp LESSTHANEQUALTO exp','exp',3,'p_exp_bin','yapl_parser.py',89),
  ('exp -> exp NOTEQUAL exp','exp',3,'p_exp_bin','yapl_parser.py',90),
  ('exp -> exp EQUALEQUAL exp','exp',3,'p_exp_bin','yapl_parser.py',91),
  ('exp -> exp AND exp','exp',3,'p_exp_bin','yapl_parser.py',92),
  ('exp -> exp OR exp','exp',3,'p_exp_bin','yapl_parser.py',93),
  ('exp -> LPAREN exp RPAREN','exp',3,'p_exp_parens','yapl_parser.py',99),
  ('exp -> exp COMMA exp','exp',3,'p_exp_comma','yapl_parser.py',105),
  ('exp -> INT','exp',1,'p_exp_num','yapl_parser.py',112),
  ('exp -> FLOAT','exp',1,'p_exp_num','yapl_parser.py',113),
  ('exp -> STRING','exp',1,'p_exp_string','yapl_parser.py',121),
  ('exp -> CHAR','exp',1,'p_exp_char','yapl_parser.py',127),
  ('exp -> BOOL','exp',1,'p_exp_bool','yapl_parser.py',133),
  ('exp -> NAME','exp',1,'p_exp_vriable','yapl_parser.py',139),
  ('stmt -> DTYPE NAME EQUAL exp SEMICOLON','stmt',5,'p_dec','yapl_parser.py',147),
  ('DTYPE -> int','DTYPE',1,'p_dec_dtype','yapl_parser.py',153),
  ('DTYPE -> string','DTYPE',1,'p_dec_dtype','yapl_parser.py',154),
  ('DTYPE -> float','DTYPE',1,'p_dec_dtype','yapl_parser.py',155),
  ('DTYPE -> bool','DTYPE',1,'p_dec_dtype','yapl_parser.py',156),
  ('DTYPE -> char','DTYPE',1,'p_dec_dtype','yapl_parser.py',157),
  ('stmt -> NAME EQUAL exp SEMICOLON','stmt',4,'p_assign','yapl_parser.py',166),
]
