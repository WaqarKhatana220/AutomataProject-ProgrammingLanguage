from yapl_lexer import *
from yapl_parser import *
import sys

# other global variables
variable_dictionary = {}

def exp_eval(p): # evaluate expression
    operator = p[0]
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
        elif operator == 'BOOL':
            return p[1]
        elif operator == 'NAME':
            if p[1] not in variable_dictionary:
                return p[1] + " used but not declared"
            else:
                return (variable_dictionary[p[1]][1])
        elif operator == 'NUM':
                return p[1]
        else:
            return p[1]


def stmt_eval(p): # p is the parsed statement subtree / program
    stype = p[0] # node type of parse tree
    if stype == 'PRINT':
        exp = p[1]
        result = exp_eval(exp)
        print(result)
    elif stype == "DECLARATION":
        exp = p[1]
        declaration_handler(exp)
    elif stype == "ASSIGNMENT":
        exp = p[2]
        if p[1] in variable_dictionary:
            result = assignment_handler(exp)
            variable_dictionary[p[1]][1] = result
            # print("after assignment", variable_dictionary)



def assignment_handler(p):
    # print("here")
    # print (p[0])
    # print (p[1])
    operator = p[0]
    if operator == '+':
        return exp_eval(p[1]) + exp_eval(p[2])
    elif operator == '-':
        return exp_eval(p[1]) - exp_eval(p[2])
    elif operator == '*':
        return exp_eval(p[1]) * exp_eval(p[2])
    elif operator == '/':
        return exp_eval(p[1]) / exp_eval(p[2])
    elif operator == 'COMMA':
        return "invalid assignment"
    else: # operator was 'NUM' so its just a number
        if operator == 'STRING':
            return (p[1][1:len(p[1])-1])
        elif operator == 'CHAR':
            return p[1][1:2]
        elif operator == 'BOOL':
            return "invalid assignment"
        elif operator == 'NAME':
            if p[1] not in variable_dictionary:
                return p[1] + " used but not declared"
            else:
                return (variable_dictionary[p[1]][1])
        elif operator == 'NUM':
                return p[1]
        else:
            return p[1]




def declaration_handler(p):
    if p[0] == "int" and type(p[2]) == int:
        if p[1] not in variable_dictionary:
            variable_dictionary[p[1]] = [p[0], p[2]]
        else:
            print("redeclaration error")
    elif p[0] == "string" and type(p[2]) == str:
        if p[1] not in variable_dictionary:
            variable_dictionary[p[1]] = [p[0], p[2]]
        else:
            print("redeclaration error")
    elif p[0] == "bool" and p[2] == 'True' or p[2] == 'False':
        if p[1] not in variable_dictionary:
            variable_dictionary[p[1]] = [p[0], p[2]]
        else:
            print("redeclaration error")
    elif p[0] == "char" and type(p[2]) == str:
        if p[1] not in variable_dictionary:
            variable_dictionary[p[1]] = [p[0], p[2]]
        else:
            print("redeclaration error")
    elif p[0] == "float" and type(p[2]) == float:
        if p[1] not in variable_dictionary:
            variable_dictionary[p[1]] = [p[0], p[2]]
        else:
            print("redeclaration error")
    else:
        print("type not matched")
    # print ("at declaration", variable_dictionary)




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