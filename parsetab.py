
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'SleftLPARENRPARENAND BOOL CHAR COMMA DIVIDE ELIF ELSE EQUAL EQUALEQUAL FLOAT FOR GREATERTHAN GREATERTHANEQUALTO IF INT LCBRACKET LESSTHAN LESSTHANEQUALTO LPAREN MINUS MINUSMINUS MODULUS MULTIPLY NAME NEXT NOT NOTEQUAL OR PLUS PLUSPLUS POWER PRINT RCBRACKET RPAREN SEMICOLON STEP STRING TO bool char float int string\n    S : stmt S\n    \n    stmt : NAME operator SEMICOLON\n    \n    operator : PLUSPLUS\n            | MINUSMINUS\n    \n    S :\n    \n    stmt : IF LPAREN exp RPAREN LCBRACKET stmt RCBRACKET\n    \n    stmt : ELIF LPAREN exp RPAREN LCBRACKET stmt RCBRACKET\n    \n    stmt : ELSE LCBRACKET stmt RCBRACKET\n    \n    stmt : PRINT LPAREN exp RPAREN SEMICOLON\n     \n    exp : exp PLUS exp\n        | exp MINUS exp\n        | exp DIVIDE exp\n        | exp MULTIPLY exp\n        | exp MODULUS exp\n        | exp POWER exp\n        | exp LESSTHAN exp\n        | exp GREATERTHAN exp\n        | exp GREATERTHANEQUALTO exp\n        | exp LESSTHANEQUALTO exp\n        | exp NOTEQUAL exp\n        | exp EQUALEQUAL exp\n        | exp AND exp\n        | exp OR exp\n    \n    exp : LPAREN exp RPAREN\n    \n    exp : NOT exp\n     \n    exp : exp COMMA exp\n    \n    exp : INT\n        | FLOAT\n    \n    exp : STRING\n    \n    exp : CHAR\n    \n    exp : BOOL\n    \n    exp : NAME\n    \n    stmt : DTYPE NAME EQUAL exp SEMICOLON\n    \n    DTYPE : int\n        | string\n        | float\n        | bool\n        | char\n    \n    stmt : NAME EQUAL exp SEMICOLON\n    \n    stmt : FOR NAME EQUAL FROM TO END stmt NEXT\n    \n    FROM : INT\n        | NAME\n    \n    END : INT\n        | NAME\n    '
    
_lr_action_items = {'$end':([0,1,2,15,26,42,62,86,87,94,95,97,],[-5,0,-5,-1,-2,-39,-8,-9,-33,-6,-7,-40,]),'NAME':([0,2,8,9,10,11,12,13,14,17,20,21,22,23,26,29,30,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,62,84,85,86,87,88,91,92,93,94,95,97,],[3,3,24,25,-34,-35,-36,-37,-38,27,27,27,3,27,-2,27,27,27,65,-39,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,-8,3,3,-9,-33,91,-44,3,-43,-6,-7,-40,]),'IF':([0,2,22,26,42,62,84,85,86,87,91,92,93,94,95,97,],[4,4,4,-2,-39,-8,4,4,-9,-33,-44,4,-43,-6,-7,-40,]),'ELIF':([0,2,22,26,42,62,84,85,86,87,91,92,93,94,95,97,],[5,5,5,-2,-39,-8,5,5,-9,-33,-44,5,-43,-6,-7,-40,]),'ELSE':([0,2,22,26,42,62,84,85,86,87,91,92,93,94,95,97,],[6,6,6,-2,-39,-8,6,6,-9,-33,-44,6,-43,-6,-7,-40,]),'PRINT':([0,2,22,26,42,62,84,85,86,87,91,92,93,94,95,97,],[7,7,7,-2,-39,-8,7,7,-9,-33,-44,7,-43,-6,-7,-40,]),'FOR':([0,2,22,26,42,62,84,85,86,87,91,92,93,94,95,97,],[9,9,9,-2,-39,-8,9,9,-9,-33,-44,9,-43,-6,-7,-40,]),'int':([0,2,22,26,42,62,84,85,86,87,91,92,93,94,95,97,],[10,10,10,-2,-39,-8,10,10,-9,-33,-44,10,-43,-6,-7,-40,]),'string':([0,2,22,26,42,62,84,85,86,87,91,92,93,94,95,97,],[11,11,11,-2,-39,-8,11,11,-9,-33,-44,11,-43,-6,-7,-40,]),'float':([0,2,22,26,42,62,84,85,86,87,91,92,93,94,95,97,],[12,12,12,-2,-39,-8,12,12,-9,-33,-44,12,-43,-6,-7,-40,]),'bool':([0,2,22,26,42,62,84,85,86,87,91,92,93,94,95,97,],[13,13,13,-2,-39,-8,13,13,-9,-33,-44,13,-43,-6,-7,-40,]),'char':([0,2,22,26,42,62,84,85,86,87,91,92,93,94,95,97,],[14,14,14,-2,-39,-8,14,14,-9,-33,-44,14,-43,-6,-7,-40,]),'EQUAL':([3,24,25,],[17,40,41,]),'PLUSPLUS':([3,],[18,]),'MINUSMINUS':([3,],[19,]),'LPAREN':([4,5,7,17,20,21,23,29,30,40,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,],[20,21,23,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,29,]),'LCBRACKET':([6,60,61,],[22,84,85,]),'SEMICOLON':([16,18,19,27,28,31,32,33,34,35,59,63,64,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,],[26,-3,-4,-32,42,-27,-28,-29,-30,-31,-25,86,87,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-26,-24,]),'NOT':([17,20,21,23,29,30,40,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,]),'INT':([17,20,21,23,29,30,40,41,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,88,],[31,31,31,31,31,31,31,67,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,93,]),'FLOAT':([17,20,21,23,29,30,40,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'STRING':([17,20,21,23,29,30,40,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'CHAR':([17,20,21,23,29,30,40,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,],[34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,]),'BOOL':([17,20,21,23,29,30,40,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,],[35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,]),'RCBRACKET':([26,38,42,62,86,87,89,90,94,95,97,],[-2,62,-39,-8,-9,-33,94,95,-6,-7,-40,]),'NEXT':([26,42,62,86,87,94,95,96,97,],[-2,-39,-8,-9,-33,-6,-7,97,-40,]),'PLUS':([27,28,31,32,33,34,35,36,37,39,58,59,64,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,],[-32,43,-27,-28,-29,-30,-31,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,43,-24,]),'MINUS':([27,28,31,32,33,34,35,36,37,39,58,59,64,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,],[-32,44,-27,-28,-29,-30,-31,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,44,-24,]),'DIVIDE':([27,28,31,32,33,34,35,36,37,39,58,59,64,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,],[-32,45,-27,-28,-29,-30,-31,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,45,-24,]),'MULTIPLY':([27,28,31,32,33,34,35,36,37,39,58,59,64,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,],[-32,46,-27,-28,-29,-30,-31,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,46,-24,]),'MODULUS':([27,28,31,32,33,34,35,36,37,39,58,59,64,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,],[-32,47,-27,-28,-29,-30,-31,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,47,-24,]),'POWER':([27,28,31,32,33,34,35,36,37,39,58,59,64,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,],[-32,48,-27,-28,-29,-30,-31,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,48,-24,]),'LESSTHAN':([27,28,31,32,33,34,35,36,37,39,58,59,64,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,],[-32,49,-27,-28,-29,-30,-31,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,49,-24,]),'GREATERTHAN':([27,28,31,32,33,34,35,36,37,39,58,59,64,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,],[-32,50,-27,-28,-29,-30,-31,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,-24,]),'GREATERTHANEQUALTO':([27,28,31,32,33,34,35,36,37,39,58,59,64,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,],[-32,51,-27,-28,-29,-30,-31,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,51,-24,]),'LESSTHANEQUALTO':([27,28,31,32,33,34,35,36,37,39,58,59,64,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,],[-32,52,-27,-28,-29,-30,-31,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,52,-24,]),'NOTEQUAL':([27,28,31,32,33,34,35,36,37,39,58,59,64,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,],[-32,53,-27,-28,-29,-30,-31,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,53,-24,]),'EQUALEQUAL':([27,28,31,32,33,34,35,36,37,39,58,59,64,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,],[-32,54,-27,-28,-29,-30,-31,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,54,-24,]),'AND':([27,28,31,32,33,34,35,36,37,39,58,59,64,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,],[-32,55,-27,-28,-29,-30,-31,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,55,-24,]),'OR':([27,28,31,32,33,34,35,36,37,39,58,59,64,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,],[-32,56,-27,-28,-29,-30,-31,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,56,-24,]),'COMMA':([27,28,31,32,33,34,35,36,37,39,58,59,64,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,],[-32,57,-27,-28,-29,-30,-31,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,57,-24,]),'RPAREN':([27,31,32,33,34,35,36,37,39,58,59,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,],[-32,-27,-28,-29,-30,-31,60,61,63,83,-25,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-26,-24,]),'TO':([65,66,67,],[-42,88,-41,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'S':([0,2,],[1,15,]),'stmt':([0,2,22,84,85,92,],[2,2,38,89,90,96,]),'DTYPE':([0,2,22,84,85,92,],[8,8,8,8,8,8,]),'operator':([3,],[16,]),'exp':([17,20,21,23,29,30,40,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,],[28,36,37,39,58,59,64,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,]),'FROM':([41,],[66,]),'END':([88,],[92,]),}

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
  ('exp -> NOT exp','exp',2,'p_exp_not','yapl_parser.py',105),
  ('exp -> exp COMMA exp','exp',3,'p_exp_comma','yapl_parser.py',111),
  ('exp -> INT','exp',1,'p_exp_num','yapl_parser.py',118),
  ('exp -> FLOAT','exp',1,'p_exp_num','yapl_parser.py',119),
  ('exp -> STRING','exp',1,'p_exp_string','yapl_parser.py',127),
  ('exp -> CHAR','exp',1,'p_exp_char','yapl_parser.py',133),
  ('exp -> BOOL','exp',1,'p_exp_bool','yapl_parser.py',139),
  ('exp -> NAME','exp',1,'p_exp_vriable','yapl_parser.py',145),
  ('stmt -> DTYPE NAME EQUAL exp SEMICOLON','stmt',5,'p_dec','yapl_parser.py',153),
  ('DTYPE -> int','DTYPE',1,'p_dec_dtype','yapl_parser.py',159),
  ('DTYPE -> string','DTYPE',1,'p_dec_dtype','yapl_parser.py',160),
  ('DTYPE -> float','DTYPE',1,'p_dec_dtype','yapl_parser.py',161),
  ('DTYPE -> bool','DTYPE',1,'p_dec_dtype','yapl_parser.py',162),
  ('DTYPE -> char','DTYPE',1,'p_dec_dtype','yapl_parser.py',163),
  ('stmt -> NAME EQUAL exp SEMICOLON','stmt',4,'p_assign','yapl_parser.py',172),
  ('stmt -> FOR NAME EQUAL FROM TO END stmt NEXT','stmt',8,'p_for_loop','yapl_parser.py',178),
  ('FROM -> INT','FROM',1,'p_for_from','yapl_parser.py',184),
  ('FROM -> NAME','FROM',1,'p_for_from','yapl_parser.py',185),
  ('END -> INT','END',1,'p_for_end','yapl_parser.py',191),
  ('END -> NAME','END',1,'p_for_end','yapl_parser.py',192),
]
