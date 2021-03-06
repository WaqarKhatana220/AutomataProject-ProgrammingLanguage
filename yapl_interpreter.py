from yapl_lexer import *
from yapl_parser import *
import sys


# other global variables
variable_dictionary = {}
global struct_dictionary
struct_dictionary = {}
global object_dictionary
object_dictionary = {}
global if_exists
if_exists = False
global if_check
if_check = True

def exp_eval(p): # evaluate expression
    operator = p[0]
    try:
        if operator == 'OBJPRINT':
            if p[1] in object_dictionary:
                if p[2] in object_dictionary[p[1]]:
                    return object_dictionary[p[1]][p[2]]
                else:
                    print("AttributeError")
                    exit(1)
            else:
                print("struct object", p[1], "does not exist")
                exit(1)
        elif operator == '+':
            return exp_eval(p[1]) + exp_eval(p[2])
        elif operator == '-':
            return exp_eval(p[1]) - exp_eval(p[2])
        elif operator == '*':
            return exp_eval(p[1]) * exp_eval(p[2])
        elif operator == '/':
            return exp_eval(p[1]) / exp_eval(p[2])
        elif operator == '%':
            return exp_eval(p[1]) % exp_eval(p[2])
        elif operator == '^':
            return exp_eval(p[1]) ** exp_eval(p[2])
        elif operator == '>':
            return exp_eval(p[1]) > exp_eval(p[2])
        elif operator == '<':
            return exp_eval(p[1]) < exp_eval(p[2])
        elif operator == '>=':
            return exp_eval(p[1]) >= exp_eval(p[2])
        elif operator == '<=':
            return exp_eval(p[1]) <= exp_eval(p[2])
        elif operator == '!=':
            return exp_eval(p[1]) != exp_eval(p[2])
        elif operator == '==':
            return exp_eval(p[1]) == exp_eval(p[2])
        elif operator == '&&':
            return exp_eval(p[1]) and exp_eval(p[2])
        elif operator == '!':
            return not exp_eval(p[1])
        elif operator == '||':
            return exp_eval(p[1]) or exp_eval(p[2])
        elif operator == 'COMMA':
            return str(exp_eval(p[1])) + " " + str(exp_eval(p[2]))
        else: # operator was 'NUM' so its just a number
            if operator == 'STRING':
                return (p[1][1:len(p[1])-1])
            elif operator == 'CHAR':
                return p[1][1:2]
            elif operator == 'BOOL':
                if p[1] == 'True':
                    return True
                elif p[1] == 'False':
                    return False
            elif operator == 'NAME':
                if p[1] not in variable_dictionary:
                    print (p[1], " used but not declared")
                    exit(1)
                else:
                    return (variable_dictionary[p[1]][1])
            elif operator == 'NUM':
                    return p[1]
            elif operator == 'PAREN':
                return p[1]
            else:
                return p[1]
    except TypeError:
        print ("TypeError")
        exit(1)
    except Exception as e:
        print (e)
        exit(1)
        


def stmt_eval(p): # p is the parsed statement subtree / program
    stype = p[0] # node type of parse tree
    global if_check
    global if_exists
    global struct_dictionary
    global object_dictionary
    if stype == 'PRINT':
        exp = p[1]
        result = exp_eval(exp)
        print(result)        
    elif stype == "DECLARATION":
        if p[2] not in variable_dictionary:
            exp = p[3]
            # print("declaration", p[1], p[2], p[3])
            result = exp_eval(exp)
            # print("result", result)
            check = declaration_handler(p[1], result)
            if check == True:
                variable_dictionary[p[2]] = [p[1], result]
            else:
                print("type not matched")
                exit(1)
        else:
            print("redeclaration error")
            exit(1)
        
        # print (variable_dictionary)p[4]
    elif stype == "STRUCTDEC":
        
        # print ("here bro", p)
        if p[1] not in struct_dictionary:
            struct_dictionary[p[1]] = {}
            for i in range(0, len(p[2])):
                exp = p[2][i]
                
                struct_dictionary[p[1]][exp[1]] = exp[0]
        else:
            print("struct", p[1], " already defined")
            exit(1)
    elif stype == "OBJDEC":
        if p[1] in struct_dictionary:
            if p[2] not in object_dictionary:
                object_dictionary[p[2]] = {}
                for keyss in struct_dictionary[p[1]]:
                    var = keyss
                    types = struct_dictionary[p[1]][keyss]
                    object_dictionary[p[2]][var] = types
                for keys in object_dictionary[p[2]]:
                    if object_dictionary[p[2]][keys] == 'int':
                        object_dictionary[p[2]][keys] = 0
                    elif object_dictionary[p[2]][keys] == 'string':
                        object_dictionary[p[2]][keys] = "s"
                    elif object_dictionary[p[2]][keys] == 'char':
                        object_dictionary[p[2]][keys] = 's'
                    elif object_dictionary[p[2]][keys] == 'float':
                        object_dictionary[p[2]][keys] = 0.2
                    elif object_dictionary[p[2]][keys] == 'bool':
                        object_dictionary[p[2]][keys] = True

            else:
                print ("object", p[2], "already defined")
                exit(1)

        else:
            print("invalid data type")
            exit(1)
    elif stype == "OBJASSIGN":

        # ('OBJASSIGN', NAME, NAME, VALUE)

        if p[1] in object_dictionary:
            if p[2] in object_dictionary[p[1]]:
                if type(object_dictionary[p[1]][p[2]]) == type(exp_eval(p[3])):
                    object_dictionary[p[1]][p[2]] = exp_eval(p[3])
                else:
                    print("TypeError")
                    exit(1)
            else:
                print("AttributeError")
                exit(1)
        else:
            print("object", p[1], "does not exist")
            exit(1)

    elif stype == "ASSIGNMENT":
        exp = p[2]
        if p[1] in variable_dictionary:
            result = exp_eval(exp)
            variable_dictionary[p[1]][1] = result
        else:
            print("variable '", p[1], "' used but not defined")
            exit(1)
    elif stype == "INC_DEC":
        if p[1] in variable_dictionary:
            result = inc_dec_calculator(p[1], p[2])
            variable_dictionary[p[1]][1] = result
        else:
            print("variable '", p[1], "' used but not defined")
            exit(1)
    elif stype == "FOR":
        start = p[2]
        stop = p[3]
        if type(start) == str:
            if start not in variable_dictionary:
                print (start, " used but not defined")
                exit(1)
            else:
                start = int(variable_dictionary[start][1])
        if type(stop) == str:
            if stop not in variable_dictionary:
                print (stop, " used but not defined")
                exit(1)
            else:
                stop = int(variable_dictionary[stop][1])
        statement = p[4]
        if p[1] not in variable_dictionary:
                variable_dictionary[p[1]] = ['int', 0]
        for i in range (start, stop):
            variable_dictionary[p[1]] = ['int', i]
            for j in range(0, len(statement)):
                statements = statement[j]
                stmt_eval(statements)

    elif stype == "CONDITIONAL":
        if_exists = True
        condition = p[2]
        statement = p[3]
        result = exp_eval(condition)
        if result == True:
            for i in range(0, len(statement)):
                statements = statement[i]
                stype = statements[0]
                stmt_eval(statements)
        else:
            if_check = False
    elif stype == "CONDITIONALELSE":
        if if_exists == True:
            if if_check == False:
                statement = p[1]
                for i in range(0, len(statement)):
                    statements = statement[i]
                    stype = statements[0]
                    stmt_eval(statements)
                if_check = True
            if_exists = False
        else:
            print("else without if")
            exit(1)


def inc_dec_calculator(vname, operator):
    if operator == "++":
        return variable_dictionary[vname][1] + 1
    if operator == "--":
        return variable_dictionary[vname][1] - 1
    else:
        return("invalid operator")


def declaration_handler(data_type, value):
    check = False
    if data_type == "int" and type(value) == int:
        check = True
    elif data_type == "string" and type(value) == str:
        check = True
    elif data_type == "bool" and type(value) == bool:
        check = True
    elif data_type == "char" and type(value) == str:
        check = True        
    elif data_type == "float" and type(value) == float:
        check = True
    else:
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