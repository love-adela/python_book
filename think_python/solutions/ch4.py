# 4.3 
# Exercise1

from TurtleWorld import *

world = TurtleWorld()
bob = Turtle()

def square(t):
    for i in range(4):
        fd(t, 100)
        lt(t)

square(bob)
wait_for_user()

# Exercise2

from TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print(bob)

def square(t, length):
    t = Turtle()
    for i in range(4):
        fd(t, length)
        lt(t)

square(bob, 200)
wait_for_user()

# Exercise3

from TurtleWorld import *

world = TurtleWorld()
bob = Turtle()
print(bob)

def polygon(t, length, n):
    t = Turtle()
    for i in range(n):
        fd(t, length)
        lt(t, 360 / n)

polygon(bob, 50, 8)
wait_for_user()
