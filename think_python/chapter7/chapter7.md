## Chapter 7. Iteration

Iteration is the ability to run a block of statements repeatedly.
There are kinds of iteration such as recursion, for loop, and while statement.

### Reassignment

A new assignment makes an existing variable refer to a new value (and stop referring to the old value).
Equality is a symmetric relationship and assignment is not.
Reassigning variables is often useful, but you should use it with caution. If the values of variables change frequently, it can make the code difficult to read and debug.

### Updating Variables

A common kind of reassignment is an update, where the new value of the variable depends on the old.
If you try to update a variable that doesn't exist, you get an error, because Python evaluates the right side before it assigns a value to x:

```
>>> x += 1
NameError: name 'x' is not defined
```

Before you can update a variable, you have to initialize it, usually with a simple assignment:
```
x = 0
x += 1 # increment

y = 10 
y -= 1 # decrement
```

### The While Statement
Because iteration is so common, Python provides language features to make it easier.

```
# countdoun uses a while statement
# While n is greater than 0, display the value of n and then decrement n.
# When you get to 0, display the word Blastoff!
def countdown(n):
    while n > 0: # while True
        print(n)
	n -= 1
    print('Blastoff!')
```

#### Flow of execution for a while statement
* Type of flow : loop
* The body of the loop should change the value of one or more variables so that the condition becomes false eventually and the loop terminates. Otherwise the loop will repeat forever, which is called an *infinite loop*. 
* Flow of execution :
	1. Determine whether the condition is true or false. 
	2. If false, exit the while statement and continue execution at the next statement.
	3. If the condition is true, run the body and then go back to step 1.

```
def sequence(n):
    while n != 1:
        print(n)
	if n % 2 == 0:
	    n /= 2
	else:
	    n = n* 3 + 1
```

```
def print_n():
    pass

```

### break
If you want to end a loop until you get halfway through the body, you can use the break statement to jump out of the loop.

```
# The loop condition is True, which is always true, so the loop runs until it hits the break statement.
# If the user types the condition, the break statement exists the loop. Otherwise the program echoes whatever the user types and goes back to the top of the loop.

def prmpt():
    while True:
        line = input('>')
	if line == 'done':
	    break
	print(line)
    print('Done!')
```

The way that the loop condition which is always true is common because you can check the condition anywhere in the loop (not just at the top) and you can express the stop condition affirmatively ('stop when this happens') rather than negatively ('keep going until that happens').


### Square Roots

Loops are often used in programs that compute numerical results by starting with an approximate answer and iteratively improving it.

```
a = 4
x = 3

while True:
    print(x)
    y = (x + a / x)  / 2
    if y == x:
        break
    x = y
```

* CAUTION : In general it is dangerous to test float equality. Floating-point values are only approximately right: most rational numbers, and irrational numbers, can't be represented exactly with a float.
Rather than checking whether x and y are exactly equal, it is safer to use the built-in function abs to compute the absolute value, or magnitude, of the difference between them:

```
if abs(y - x) < epsilon:
    break
```

Where epsilon has a value, like 0.0000001, that determines how close is close enough.


### Algorithms

Algorithm is a mechanical process for solving a category of problems.

- Examples
  - To find the produc of n and 9
  - addition with carrying
  - subtraction with borrowing
  - long division

### Debugging

One way to cut your debugging time is "debugging by bisection".


