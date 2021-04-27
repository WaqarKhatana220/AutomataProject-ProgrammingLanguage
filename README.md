# AutomataProject-ProgrammingLanguage
I built a custom programming language called YAPL (Yet Another Programming Language) using lex and yacc in python for my course Theory of Automata.

## Functionality
The language supports following features;

**Variable declaration and assignment**

**Conditionals (if/else)**

**For loops**

**Struct**

## Syntax

Print Statement:

```
print ("hello");
```

Variable Declaration:

```
data-type variableName = value;
```

The following data types are supported;

`int` `float` `string` `char` `bool`

After declaration, you can reassign a value to a variable as;

```
variableName = new value;
```

Conditional:

YAPL supports if else only, the syntax is as follows;

```
if (condition)
{if block}
else
{else block}
```You can run the YAPL interpreter with the command
87


Logical operators `And` `Or` and `Not` are supported.

For Loops:

The For loop syntax is as follows;

```
for a = x to y
statements to execute
next
```

Struct:
Declare a struct as;

```
struct structName
{
data-type variableName;
}
```

declare struct object as;

```
structName objectName;
```

assign values to attributes as;

```
objectName -> attributeName = value;
```

## Run

Download the files in your local machine. Open the terminal in the directory where you have downloaded the files and give the following command;

```
python3 yapl_interpreter.py filename.txt
```

There are a number of test files in the `test_cases` directory which you can give at the command line to run. Alternatively, you can also create a custom .txt file and test it using the same command.
