import ply.yacc as yacc
from yapl_lexer import *

#sys.tracebacklimit = 0 # to prevent traceback debug output since it is not needed

# to resolve ambiguity, individual tokens assigned a precedence level and associativity. 
# tokens ordered from lowest to highest precedence, rightmost terminal judged


start = 'S'
# multiple variables, assigning data from one variable to another

# after the lexing, start parsing

def p_start(p): # non-terminal, starting
    """
    S : stmt S
    """
    p[0] = [p[1]] + p[2] # list comprehension used to solve recursive grammar, added/appending as well
    

def p_start_empty(p):
    """
    S :
    """
    p[0] = []


def p_print_stmt(p):
    """
    stmt : PRINT LPAREN exp RPAREN SEMICOLON
    """
    p[0] = ('PRINT', p[3])

def p_exp_bin(p):
    """ 
    exp : exp PLUS exp
        | exp MINUS exp
        | exp DIVIDE exp
        | exp MULTIPLY exp
    """
    p[0] = (p[2], p[1], p[3]) # '1+2' -> ('+', '1', '2')

def p_exp_comma(p):
    """ 
    exp : exp COMMA exp
    """
    p[0] = ('COMMA', p[1] , p[3]) # '1+2' -> (',', '1', '2')


def p_exp_num(p):
    """
    exp : INT
        | FLOAT
    """
    p[0] = ('NUM', p[1])
    
def p_exp_string(p):
    """
    exp : STRING
    """
    p[0] = ('STRING', p[1])

def p_exp_char(p):
    """
    exp : CHAR
    """
    p[0] = ('CHAR', p[1])

def p_exp_bool(p):
    """
    exp : BOOL
    """
    p[0] = ('BOOL', p[1])

def p_exp_vriable(p):
    """
    exp : NAME
    """
    p[0] = ('NAME', p[1])

def p_dec(p):
    """
    stmt : DTYPE NAME EQUAL exp SEMICOLON
    """
    p[0] = ('DECLARATION',p[1], p[2], p[4])
    print(p[0])

def p_dec_dtype(p):
    """
    DTYPE : int
        | string
        | float
        | bool
        | char
    """
    p[0] = p[1]



def p_assign(p):
    """
    stmt : NAME EQUAL exp SEMICOLON
    """
    p[0] = ('ASSIGNMENT', p[1], p[3])

# def inc_dec_rement(p):
#     """
#     stmt : NAME exp
#     """
#     p[0] = 

def p_error(p):
    print("Syntax error at token", p.value, p.type, p.lexpos)
    exit(1)

parser = yacc.yacc() # start parsing, yacc object created