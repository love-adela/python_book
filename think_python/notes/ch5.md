## Chapter 5. Conditionals and Recursion

### 5.1 Floor Division and Modulus

Floor division returns the integer number of hours, dropping the fraction part.

#### Express minutes in hours
* Get hour
  * hours = minutes // 60
* Get the remainder
  * remainder = minutes - hours * 60
  * remainder = minutes % 60

#### Modulus operator ``` % ```
* Usages
  * You can check whether one number is divisible by another.
    * ```if x % y == 0: x % y == 0```

  * You can extract the right-most digit or digits from a number.
    * ``` x % 10 ``` : yields the right-most digit of x (in base 10)
    * ``` x % 100 ``` : yields the last two digits.

### 5.2 Boolean Expressions

A boolean expression is an expression that is either true or false.o

* True and False
  * type : <class 'bool'>

* Relational operators

  * ```x  == y```
  * ```x != y```
  * ```x > y```
  * ```x < y```
  * ```x >= y```
  * ```x <= y```

### 5.3 Logical Operators
* and
* or
* not

#### Flexibility of the local operator
Strictly the operands of the logical operators should be boolean expressions, but Python is not very strict. Any nonzero number is interpreted as True.

```
>>> 42 and True
True
```

### 4.3 Conditional Execution
In order to write useful programs, we almost always need the ability to check conditions and change the behavior of the program accordingly. Conditional statements give us this ability.

```
if x > 0:
    print('x is positive')
```

If the condition is true, the indented statement runs. If not, nothing happens.

#### if statement structure
It is the same as function definitions.

A header followed by an indented body. Statements like this are called compound statements.

#### pass statement
Occasionally it is useful to have a body with no statements. In that case, you can use the pass statement, which does nothing.

```
if x < 0:
    pass # need to handle negative values!
```

### 4.4 Alternative Execution
There are two possibilities and the condition determines which one runs, and this form of the if statement is 'alternative execution'.

```
if x % 2 == 0:
    print('x is even')
else:
    print('x is odd')
```

Since the condition must be true or false, exactly one of the alternatives will run. The alternatives are called branches.

### 4.5 Chained Conditionals
Sometimes there are more than two possibilities and we need more than two branches. 
Each condition is checked in order. 
If the first if false, the next is checked, and so on.
If one of them is true, the corresponding branch runs and the statement ends.
Even if more than one condition is true, only the first true branch runs.

#### chained conditionals 
One way to express a computation like that is a chained conditional.

```
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal.')
```

#### elif
elif is abbreviation of 'else if'. Again exactly one branch will run. There is no limit on the number of elif statements. If there is an else clause, it has to be at the end, but there doesn't have to be one.

```
if choice == 'a':
    draw _a()
elif choice == 'b':
    draw _b()
elif choice == 'c':
    draw _c()
```

### 4.6 Nested Conditionals

One conditional can also be nested within another. 

#### Indentation

Although the indentation of the statements makes the structure apparent, nested conditionals become difficult to read very quickly. It is a good idea to avoid them when you can.

#### Logical operator

Logical operators often provide a way to simplify nested conditional statements. 

```
# single conditional
if 0 < x:
    if x < 10:
        print('x is positive single-digit number.')

# nested conditionals using and operator
if 0 < x and x < 10:
    print('x is a positive single-digit number.')

# pythonic code
if 0 < x < 10:
    print('x is a positive single-digit number.')
```

### 4.7 Recursion

It is legal for one function to call another; it is also legal for a functio to call itself.

```
def countdown(n):
    if n <= 0: print('Blast off!')
    else: 
        print(n)
	countdown(n-1)

# Write a function that prints a string n times:

def print_n(s, n):
    if n <= 0:
        return 
    print(s)
    print_n(s, n-1)
```

