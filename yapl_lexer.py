import ply.lex as lex
import re

# TOKEN IDENTIFIERS, have to match name of our token

# list of all possible tokens
tokens = [
    'INT',
    'PLUS',
    'MINUS',
    'SEMICOL',
    'PRINT'
]

t_PLUS = r'\+' # recognise regular expression symbol
t_MINUS = r'\-'
t_SEMICOL = r'\;'
t_ignore = ' \t\r\n\f\v' # ignore spaces, better lexing performance, special case

# variable or function names (including predefined functions like print)
def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value == 'print':
        t.type = 'PRINT'
    else:
        t.type = 'NAME'
        
    return t


def t_INT(t): # parameter t is the token
    r'\d+' # atleast one digit
    t.value = int(t.value) # convert to int
    return t


def t_lineno(t):
    r'\n'
    t.lexer.lineno += len(t.value) 


def t_error(t): # error while lexing
    print("[Lexer Error] Line",t.lineno)
    print(f"Illegal character: {t.value}")
    t.lexer.skip(1) # skips illegal character

# create lexer
lexer = lex.lex()

# ENABLE THIS TO TEST YOUR LEXER DIRECTLY
# while True:
#     print("YAPL_LEXER>>",end='')
#     lexer.input(input()) # reset lexer, store new input
        
#     while True: # necessary to lex all tokens
#         tokenEntered = lexer.token() # return next token from lexer
#         if not tokenEntered: # lexer error also given
#             break
#         print(tokenEntered)
