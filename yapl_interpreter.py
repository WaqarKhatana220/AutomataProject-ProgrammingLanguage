from yapl_lexer import *
from yapl_parser import *
import sys

# other global variables

def exp_eval(p): # evaluate expression
    operator = p[0]

    # if operator == 'NUM':
    #     print ("NUM H")
    # if operator == 'STRING':
    #     print ("STRING H")
    # if operator == 'CHAR':
    #     print ("CHAR H")
    # if operator == 'COMMA':
    #     print ("COMMA H")
    if operator == '+':
        return exp_eval(p[1]) + exp_eval(p[2])
    elif operator == '-':
        return exp_eval(p[1]) - exp_eval(p[2])
    elif operator == '*':
        return exp_eval(p[1]) * exp_eval(p[2])
    elif operator == '/':
        return exp_eval(p[1]) / exp_eval(p[2])
    elif operator == 'COMMA':
            return exp_eval(p[1]) , exp_eval(p[2])
    else: # operator was 'NUM' so its just a number
        if operator == 'STRING':
            return (p[1][1:len(p[1])-1])
        elif operator == 'CHAR':
            return p[1][1:2]
        else:
            return p[1]


def stmt_eval(p): # p is the parsed statement subtree / program
    stype = p[0] # node type of parse tree
    if stype == 'PRINT':
        exp = p[1]        
        result = exp_eval(exp)
        print(result)


def run_program(p): # p[0] == 'Program': a bunch of statements
    for stmt in p: # statements in proglist
        if stmt != None:
            stmt_eval(stmt) # statement subtree as tuple
        

if len(sys.argv) == 1:
    print('File name/path not provided as cmd arg.')
    exit(1)

while True:
    fileHandler = open(sys.argv[1],"r")
    userin = fileHandler.read()
    fileHandler.close()

    print("Welcome to your YAPL's Interpreter!")
    parsed = parser.parse(userin)
    if not parsed:
        continue
    
    for line in userin.split('\n'):
        print(line)
    print("=========================================\n{OUTPUT}")
    try:
        run_program(parsed)
    except Exception as e:
        print(e)
    
    input("Press any key to run code again.")


exit()