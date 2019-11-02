import math
from TurtleWorld import *
import turtle

if __name__ == '__main__':

    bob = turtle.Turtle()
    bob.delay = 0.1

    radius = 100
    bob.pu()
    bob.fd(radius)
    bob.lt(90)
    bob.pd()
    bob.circle(radius)

    input()
