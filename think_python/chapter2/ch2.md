# Chapter2

## Variables, Expressions and Statements 

A variable is a name that refers to a value

### Assignment Statements

* Assignment Statements creates a new variable and gives it a value.
  * The assignment statement produces no output in the Python interpreter.

#### State diagram

The figure is that a common way to represent variables on paper is to write the name with an arrow pointing to its value. It shows what state each of the variables is in 

### Variable Names
* They can contain both letters and numbers, but they can't begin with a number.  
* It is legal to use uppercase letters, but it is conventional to use only lowercase for variables names.
* The underscore character, _, is often used in names with multiple words.
* Syntax Error : invalid syntax

#### Keywords
The interpreter uses keywords to recognize the structur of the program, and they can't be used as variable names.
 
* Example
: False, class, finally, is, return, None, continue, for, lambda, try, True, def, from, nonlocal, while, and, del, global, not, with, as, elif, if, out, yield, assert, else, import, pass, break, except, in, raise

### Expressions and Statements
* Expression is a combination of values, variables, and operators.
  * Interpreter **evaluates** an expression at the prompt.
* Statement is a unit of code that has an effect.
  * Creating a variable or displaying a value.
  * Interpreter **exectues** a statement.

### Script Mode
[ThinkPython2E](http://tinyurl.com/thinkpython2e)

### Order of Operations

Python follows mathematical convention. 

* Parentheses have the highest precedence and can be used to force an expression to evaluate in the order you want.

* Exponentiation has the next highest precedence.

* Multiplication and Division have higher precedence than Addition and Subtraction.

* Operators with the same precedence are evaluated from left to right (except exponentiation).

### String Operations

* In general, you can't perform mathematical operations on strings. BUt there are two exceptions, +, and *.

### Comments
 
* Comments that are notes and they start with # symbol.
* To reduce comments, make good variable names. But long names can make complex expressions hard to read, so ther is a trade-off.

### Debugging

