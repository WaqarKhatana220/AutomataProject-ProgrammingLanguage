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
        if p[2] not in variable_dictionary:
            exp = p[3]
            result = exp_eval(exp)
            # print("result", result)
            check = declaration_handler(p[1], result)
            if check == True:
                variable_dictionary[p[2]] = [p[1], result]
            else:
                print("type not matched")
        else:
            print("redeclaration error")
        # print (variable_dictionary)
    elif stype == "ASSIGNMENT":
        exp = p[2]
        if p[1] in variable_dictionary:
            result = exp_eval(exp)
            variable_dictionary[p[1]][1] = result
            # print("after assignment", variable_dictionary)





def declaration_handler(data_type, value):
    check = False
    if data_type == "int" and type(value) == int:
        # print("data_type", data_type, "value", value)
        check = True
    elif data_type == "string" and type(value) == str:
        # print("data_type", data_type, "value", value)
        check = True
    elif data_type == "bool" and value == 'True' or value == 'False':
        # print("data_type", data_type, "value", value)
        check = True
    elif data_type == "char" and type(value) == str:
        # print("data_type", data_type, "value", value)
        check = True        
    elif data_type == "float" and type(value) == float:
        # print("data_type", data_type, "value", value)
        check = True
    else:
        # print("data_type", data_type, "value", value)
        check = False
    return check




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