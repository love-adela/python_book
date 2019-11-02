positional argument : . 

keyword argument: If you write parameter name that would be keyword argument.

def move(x=10, y=20):
    pass

move(30, 40)
30: positional argument -> x
40: positional argument -> y

move(30, y=40)
30: positional argument -> x
y=40: keyword argument -> y

move(x=30, y=40)
both all: keyword argument

move(y=40)
y=40: keyword argument

move(5)
5: positional argument

move(x=5)
x=5: keyword argument

parameter : 함수 / method를 정의할 때
argument : 함수를 호출할 때 넘기는 값
호출할

### operator overloading 

When you apply the + operator to Time objects, Python invokes __add__. When you print the result, python invokes __str__. 

It is changing the behavior of an operator so that it works with programmer-defined types.

For every operator in Python there is a corresponding special method, like __add__. 

### Type-Based Dispatch

: Built-in function isinstance takes a value and a class object, and returns True if the value is an instance of the class.
Type-based dispatch is an operation that dispatches the computation to different methods based on the type of the arguments.

isinstance()

#### __radd__ method : "right-side add"

This method is invoked when a Time object appears on the right side of the + operator.

