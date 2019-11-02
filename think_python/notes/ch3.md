# Chapter3. Functions

A function is a named sequence of statements that performs a computation.

When you define a function, you specify the name and the sequence of statements. 

## 3.1 Function Calls
### 3.1.1 Composition of function
```
>>> type(42)
<class 'int'>
```

* Name of the function 
  * type
* Argument of the function
  * 42
* Result
  * int

A function 'takes' an argument and 'returns' a result.
The result is also called the return value.

### 3.1.2 Type Casting
Python provides functions that convert values from one type to another. The int function takes any value and converts it to an integer.

#### 3.1.2.1 int()
```
>>> int('32')
32
>>> int('Hello')
Value Error: invalid literal for int(): Hello
```

int can convert floating-point values to integers, but it doesn't roud off;
it chops off the fraction part:

```
>>> int(3.99999)
3
>>> int(-2.3)
-2
```
#### 3.1.2.2 float()
float converts integers and strings to floating-point numbers:
```
>>> float(32)
32.0
>>> float('3.14159')
3.14159
```
#### 3.1.2.3 str()

```
>>> str(32)
'32'
>>> str(3.14159)
'3.14159'
```

## 3.2 Math Functions

### 3.2.1 Module
Python has a math module.
A module is a file that contains a collection of related functions.

Before we can use the functions in a module, we have to import it with an import statement.

```
>>> import math
>>> math
<module 'math' (built-in)>
```
Statement creates a module object named math. 
The module object contains the funtions and variables defined in the module.

### 3.2.2 How to access one of the funtions in the module

### 3.2.2.1 Dot notation
To access you have to specify the name of the module and the name of the function, separated by a dot.

```
>>> ration = signal_power / noise_power
>>> decibels = 10 * math.log10(ratio) # The math module also provides log, which computes logarithms base e.

>>> radians = 0.7
>>> height = math.sin(radians)

>>> degrees = 45
>>> radians = degrees / 180.0 * math.pi
>>> math.sin(radians)
0.7071067811865475

>>> math.sqrt(2) / 2.0
0.707106781187
```

## 3.3 Composition
To combine the elements of a program- variables, expressions, and statements, you can take small building blocks and compose them.

### 3.3.1 Composition : take small building blocks
The argument of a function can be any kind of expression , including arithmetic operators.

```
x = math.sin(degrees / 360.0 * 2 * math.pi) # The argument of a function can be arithmetic operators.
x = math.exp(math.log(x + 1)) # Function calls
```

### 3.3.2 Assignment statement

Almost anywhere you can put a value, you can put an arbitrary expression, with one exception: the left side of an assignment statement has top be a variable name.

```
>>> minutes = hours * 60 # right
>>> hours * 60 = minutes # wrong
SyntaxError: can't assign to operator
```

## 3.4 Adding New Functions
Defining a function creates a function object, which has type function:

```
>>> print(print_lyrics)
<function print_lyrics at 0xb7e99e9c>
>>> type(print_lyrics)
<class 'function'>
```

### 3.4.1 Function Definition

A function definition specifies the name of a new function and the sequence of statements that run when the function is called.

```
def print_lyrics():
    print("I'm a lumberjack, and I'm okay.")
    print("I sleep all night and I work all day.")
```

* ```def``` keyword
: def is a keyword that indicates that this is a function definition.

* Rule of a function name
  * Same as for variable names
    * Letters, numbers and underscore are legal
    * First character can't be a number 
    * You can't use a keyword as the name of a function.

* () Empty parentheses after the name
: These indicate that this function doesn't take any arguments.

* Header and Body
  * Header : The first line of the function definition
    * It has to end with a colon ```:``` 
  * Body : The rest of the function definition
    * It has to be indented.
    * Indentation is alwayf four spaces.
    * The body can contain any number of statements.

### 3.4.2 Print statements

* Quotation mark
  * The strings in the print statements are enclosed in double quotes. 
  * Single quotes and double quotes do the same thing.
  * All quotation marks (single and double) must be "Straight quotes", usually located next to Enter on the keyboard.
  * "Curly quotes" are not legal in Python.

### 3.4.3 ...

If you type a function definition in interactive mode, the interpreter prints dots (...) to let you know that the definition isn't complete.

To end the function, you have to enter an empty line. 

### 3.4.4 Calling the new function

Once you have defined a function, you can use it inside another function.

## 3.5 Definitions and Uses

Function definitions get executed just like other statements, but the effect is to create function objects, but the effect is to create function objects.

## 3.6 Flow of Execution

Flow of execution is the order statements run in to ensure that a function is defined before its first use.
When you read a program, you don't always want to read from top to bottom. 
Sometimes it makes more sense if you follow the flow of exeucution.

### 3.6.1 Execution

Execution always begins at the first statement of the program. 
Statements are run one at a time, in order from top to bottom.
Function definitions don't alter the flow of execution of the program.

### 3.6.2 Function Call
If the function isn't called statements inside the function don't run.  
A function call is like a detour in the flow of execution.

* Instead of going to the next statement, the flow jumps to the body of the function, runs the statements there, and then comes back to pick up where it left off.

* If one function call another, the program might have to run the statements in another functino while in the middle of one function. Then while running that new function, the program might have to run yet another function.

  * Fortunately, Python is good at keeping track of where the program is, so each time a function completes, the program picks up where it left off in the function that called it. 
    When it gets to the end of the program, it terminates.

## 3.7 Parameters and Arguments

Inside the function, the arguments are assigned to variables called parameters.

```
""" The function works with any value that can be printed.
Its type can be string, integer, or another function like math.pi.
"""
def print_twice(bruce):
    print(bruce)
    print(bruce)

```

The same rules of composition that apply to built-in functions also apply to programmer-defined functions, so we can use any kind of expression as an argument for the function.

```
>>> print_twice('Spam '*4)
Spam Spam Spam Spam
Spam Spam Spam Spam

>>> print_twice(math.cos(math.pi))
-1.0
-1.0
```

You can also use a variable as an argument.

## 3.8 Variables and Parameters Are Local
When you create a variable inside a function, it is local. 
It means that it only exists inside the function.

```
def cat_twice(part1, part2):
    cat = part1 + part2
    print_twice(cat)
```

When cat_twice terminates, the variable cat is destroyed. 
If we try to print it, we get an exception:

```
print(cat)
NameError: name 'cat' is not defined.
```

Parameters are also local. For example, outside print_twice, there is no such thing as bruce.

## 3.9 Stack Diagrams
To keep track of which variables can be used where, it is sometimes useful to draw a stack diagram.
Like state diagrams, stack diagrams show the value of each variable, but they also show the function each variable belongs to.

Each function is represented by a frame.
A frame is a box with the name of a function beside it and the parameters and variables of the function inside it.

### 3.9.1 __main__

__main__ function is a special name for the topmost frame. When you create a variable outisde of any function, it belongs to __main__.

Each parameter refers to the same value as its corresponding argument. 

If an error occurs during a function call, Python prints the name of the function, the name of the function that called it, and the name of the function that called that, all the way back to __main__.

### 3.9.2 traceback

Traceback is the list of functions. It tells you what program file the error occurred in, and what line, and what functions were executing at the time. It also shows the line of code that caused the error.

```
Traceback(innermost last):
  File "test.py", line 13, in __main__
    cat_twice(line1, line2)
  File "test.py", line 5, in cat_twice
    print_twice(cat)
  File "test.py", line 9, in print_twice
    print(cat)
NameError: name 'cat' is not defined.
```

The order of the functions in the traceback is the same as the order of the frames in the stack diagram.
The function that is currently running is at the bottom.

## 3.10 Fruitful Functions and Void Functions

### 3.10.1 Fruitful Functions
Fruitful Function is the function return result.

When you call a fruitful function, you almost always want to do something with the result; for example, you might assign it to a variable or use it as part of an expression.

```
x = math.cos(radians)
golden = (math.sqrt(5) + 1) / 2
```

Unlike in interactive mode, in a script, if you call a fruitful function all by itself, the return value is lost forever.

### 3.10.2 Void Functions
Void function is the function don't return a value.

Void functions might display something on the screen or have some other effect, but they don
t have a return value. 
If you assign the result to a variable, you get a special value called None:

The value None is not the same as the string 'None'. 
```
>>> result = print_twice('Bing')
Bing
Bing
>>> print(result)
None
```

The value None is not the same as the string 'None'. 
It's a special value that has its own type: 

```
>>> print(type(None))
<class 'NoneType'>
```

## 3.11 Why Functions?
Reasons why it is worth the trouble to divide a program into functions.

* Creating a new function gives you an opportunity to name a group of statements, which makes your program easier to read and debug.
* Functions can make a program smaller by eliminating repetitive code. Later, if you make a change, you only have to make it in one place.
* Dividing a long program into functions allows you to debug the parts one at a time and then assemble them into a working whole.
* Well-designed functions are often useful for many programs. Once you write and debug one, you can reuse it.

