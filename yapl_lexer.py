import ply.lex as lex
import re

tokens = [
    'INT',
    'STRING',
    'FLOAT',
    'CHAR',
    'BOOL',
    'PLUS',
    'MINUS',
    'DIVIDE',
    'MULTIPLY',
    'POWER',
    'MODULUS',
    'PLUSPLUS',
    'MINUSMINUS',
    'LESSTHAN',
    'GREATERTHAN',
    'LESSTHANEQUALTO',
    'GREATERTHANEQUALTO',
    'NOTEQUAL',
    'EQUALEQUAL',
    'NOT',
    'AND',
    'OR',
    'LPAREN',
    'RPAREN',
    'SEMICOLON',
    'EQUAL',
    'PRINT',
    'COMMA',
    'string',
    'int',
    'float',
    'bool',
    'char',
    'NAME'
]

t_PLUSPLUS = r'\+\+'
t_MINUSMINUS = r'\-\-'
t_PLUS = r'\+'
t_MINUS = r'\-'
t_DIVIDE = r'/'
t_MULTIPLY = r'\*'
t_POWER = r'\^'
t_MODULUS = r'\%'
t_LESSTHANEQUALTO = r'\<='
t_GREATERTHANEQUALTO = r'\>='
t_LESSTHAN = r'\<'
t_GREATERTHAN = r'\>'
t_NOTEQUAL = r'\!='
t_EQUALEQUAL = r'\=='
t_NOT = r'\!'
t_AND = r'\&\&'
t_OR = r'\|\|'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r'\;'
t_EQUAL = r'\='
t_STRING = r'\".*?\"'
t_CHAR = r'\'[a-zA-Z_0-9]\''
t_COMMA = r'\,'
t_ignore = ' \t\r\n\f\v' # ignore spaces, better lexing performance, special case


def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value == 'print':
        t.type = 'PRINT'
    elif t.value == "True" or t.value == "False":
        t.type = 'BOOL'
    elif t.value == 'string':
        t.type = 'string'
    elif t.value == 'int':
        t.type = 'int'
    elif t.value == 'float':
        t.type = 'float'
    elif t.value == 'bool':
        t.type = 'bool'
    elif t.value == 'char':
        t.type = 'char'
    else:
        t.type = "NAME"
        
    return t


def t_FLOAT(t):
    r'(\d*\.\d+)|(\d+\.\d*)'
    t.value = float(t.value)
    return t


def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t



def t_lineno(t):
    r'\n'
    t.lexer.lineno += len(t.value) 


def t_error(t): # error while lexing
    print("[Lexer Error] Line",t.lineno)
    print(f"Illegal character: {t.value}")
    t.lexer.skip(1) # skips illegal character


lexer = lex.lex()

# while True:
#     print("YAPL_LEXER>>",end='')
#     lexer.input(input()) # reset lexer, store new input
        
#     while True: # necessary to lex all tokens
#         tokenEntered = lexer.token() # return next token from lexer
#         if not tokenEntered: # lexer error also given
#             break
#         print(tokenEntered)