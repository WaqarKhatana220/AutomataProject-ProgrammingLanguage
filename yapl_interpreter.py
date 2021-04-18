from yapl_lexer import *
from yapl_parser import *
import sys

# other global variables
variable_dictionary = {}
struct_dictionary = {}
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
                    print("attribute", p[2], "does not exist")
            else:
                print("struct object", p[1], "does not exist")
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
                    return p[1] + " used but not declared"
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
        return e
        


def stmt_eval(p): # p is the parsed statement subtree / program
    stype = p[0] # node type of parse tree
    global if_check
    global if_exists
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
        else:
            print("redeclaration error")
        # print (variable_dictionary)
    elif stype == "STRUCTDEC":
        if p[1] not in struct_dictionary:
            exp = p[2]
            struct_dictionary[p[1]] = {}
            struct_dictionary[p[1]][exp[1]] = exp[0]
            print ("here", struct_dictionary)
        else:
            print("struct", p[1], " already defined")
    elif stype == "OBJDEC":
        if p[1] in struct_dictionary:
            if p[2] not in object_dictionary:
                object_dictionary[p[2]] = struct_dictionary[p[1]]
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
                    # print("object_dictionary[p[2]][keys]", object_dictionary[p[2]][keys])

            else:
                print ("object", p[2], "already defined")
        else:
            print("invalid data type")
    elif stype == "OBJASSIGN":
        if p[1] in object_dictionary:
            if p[2] in object_dictionary[p[1]]:
                print("ok", object_dictionary)
                exp = p[3]
                result = exp_eval(exp)
                # print("this", object_dictionary[p[1]][p[2]])
                if type(object_dictionary[p[1]][p[2]]) == type(result):
                    object_dictionary[p[1]][p[2]] = result
                    print("done")    
                else:
                    print("TypeError")
                # print ("struct_dictionary", struct_dictionary)
                # print ("object_dictionary", object_dictionary)
                # print ("result", result)

            else:
                print ("attribute", p[2], "does not exist")
        else:
            print("struct object", p[1], "does not exist")
    elif stype == "PRINTOBJ":
        if p[1] in object_dictionary:
            if p[2] in object_dictionary[p[1]]:
                print(object_dictionary[p[1]][p[2]])
    elif stype == "ASSIGNMENT":
        exp = p[2]
        if p[1] in variable_dictionary:
            result = exp_eval(exp)
            variable_dictionary[p[1]][1] = result
            # print("after assignment", variable_dictionary)
        else:
            print("variable '", p[1], "' used but not defined")
    elif stype == "INC_DEC":
        if p[1] in variable_dictionary:
            result = inc_dec_calculator(p[1], p[2])
            variable_dictionary[p[1]][1] = result
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
            stmt_eval(p[4])

    elif stype == "CONDITIONAL":
        if_exists = True
        local_variable_dictionary = {}
        level = p[1]
        condition = p[2]
        statement = p[3]
        result = exp_eval(condition)
        if result == True:
            stype = statement[0]
            stmt_eval(p[3])
        else:
            if_check = False
    elif stype == "CONDITIONALELSE":
        if if_exists == True:
            if if_check == False:
                local_variable_dictionary = {}
                statement = p[1]
                stype = statement[0]
                stmt_eval(p[1])
                if_check = True
            if_exists = False
        else:
            print("else without if")

    # print(variable_dictionary)   




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
        # print("data_type", data_type, "value", value)
        check = True
    elif data_type == "string" and type(value) == str:
        # print("data_type", data_type, "value", value)
        check = True
    elif data_type == "bool" and type(value) == bool:
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