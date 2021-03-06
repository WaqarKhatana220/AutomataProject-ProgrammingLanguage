import ply.yacc as yacc
from yapl_lexer import *

#sys.tracebacklimit = 0 # to prevent traceback debug output since it is not needed

# to resolve ambiguity, individual tokens assigned a precedence level and associativity. 
# tokens ordered from lowest to highest precedence, rightmost terminal judged


precedence = (
    ('left', 'LPAREN', 'RPAREN'), # +, - same precedence, left associative
    # ('left', 'POWER', 'PLUSPLUS', 'MINUSMINUS',
    # 'MULTIPLY', 'DIVIDE', 'MODULUS',
    # 'PLUS', 'MINUS',
    # 'EQUALEQUAL', 'NOTEQUAL', 'GREATERTHAN', 'GREATERTHANEQUALTO',
    # 'LESSTHAN', 'LESSTHANEQUALTO', 
    # 'NOT', 'AND', 'OR')
)


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

def p_struct_dec(p):
    """
    stmt : STRUCT NAME LCBRACKET statement RCBRACKET
    """
    p[0] = ('STRUCTDEC', p[2], p[4])    # ('STRUCT', NAME, stmt)

def p_struct_dec_statement(p):
    """
    statement : DTYPE NAME SEMICOLON statement
    """
    p[0] = [(p[1], p[2])] + p[4]


def p_struct_dec_statement_empty(p):
    """
    statement : 
    """
    p[0] = []


def p_obj_dec(p):
    """
    stmt : NAME NAME SEMICOLON
    """
    p[0] = ('OBJDEC', p[1], p[2])

def p_obj_assignment(p):
    """
    stmt : NAME ARROW NAME EQUAL exp SEMICOLON
    """
    p[0] = ('OBJASSIGN', p[1], p[3], p[5]) # ('OBJASSIGN', NAME, NAME, VALUE)

def p_inc_dec_rement(p):
    """
    stmt : NAME operator SEMICOLON
    """
    p[0] = ("INC_DEC", p[1], p[2])

def p_operator(p):
    """
    operator : PLUSPLUS
            | MINUSMINUS
    """
    p[0] = p[1]

def p_conditional_if(p):
    """
    stmt : IF LPAREN exp RPAREN LCBRACKET stmts RCBRACKET
    """
    p[0] = ('CONDITIONAL', p[1], p[3], p[6])

def p_conditional_else(p):
    """
    stmt : ELSE LCBRACKET stmts RCBRACKET
    """
    p[0] = ('CONDITIONALELSE', p[3])

def p_stmts(p):
    """
    stmts : stmt stmts
    """
    p[0] = [p[1]] + p[2]

def p_stmts_empty(p):
    """
    stmts : 
    """
    p[0] = []


def p_conditional_elif(p):
    """
    stmt : ELIF LPAREN exp RPAREN LCBRACKET stmt RCBRACKET
    """
    p[0] = ('CONDITIONALELIF', p[1], p[3], p[6])



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
        | exp MODULUS exp
        | exp POWER exp
        | exp LESSTHAN exp
        | exp GREATERTHAN exp
        | exp GREATERTHANEQUALTO exp
        | exp LESSTHANEQUALTO exp
        | exp NOTEQUAL exp
        | exp EQUALEQUAL exp
        | exp AND exp
        | exp OR exp
    """
    p[0] = (p[2], p[1], p[3]) # '1+2' -> ('+', '1', '2')

def p_exp_obj(p):
    """
    exp : NAME ARROW NAME
    """
    p[0] = ('OBJPRINT', p[1], p[3])

def p_exp_parens(p):
    """
    exp : LPAREN exp RPAREN
    """
    p[0] = p[2]

def p_exp_not(p):
    """
    exp : NOT exp
    """
    p[0] = (p[1], p[2])



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

def p_for_loop(p):
    """
    stmt : FOR NAME EQUAL FROM TO END stmts NEXT
    """
    p[0] = ("FOR", p[2], p[4], p[6], p[7], p[8]) #(FOR, NAME, INT, INT, stmt, NEXT)

def p_for_from(p):
    """
    FROM : INT
        | NAME
    """
    p[0] = p[1]

def p_for_end(p):
    """
    END : INT
        | NAME
    """
    p[0] = p[1]

def p_error(p):
    print("Syntax error at token", p.value, p.type, p.lexpos)
    exit(1)

parser = yacc.yacc() # start parsing, yacc object created