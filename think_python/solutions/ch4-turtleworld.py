import turtle
import math

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)


def polyline(t, n, length, angle):
    """Draws n line segments.
    t: Turtle object
    n: number of line segments
    length: length of each segment
    angle: degrees between segments
    """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length, angle):
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    angle = 360.0 / n
    polyline(t, n, length, angle)


def arc(t, r, angle):
    arc_length = (2 * math.pi * r) * (angle / 360)
    n = int(arc_length/4) + 3
    step_length = arc_length / n
    step_angle = float(angle)/n

    t.lt(step_angle / 2)
    polyline(t, n, step_length, step_angle)
    t.rt(step_angle / 2)


def circle(t, radius):
    arc(t, radius, 360)


def main():
    bob = turtle.Turtle()
    bob.delay = 0.005
    square(bob,45)
    square(bob,100)
    square(bob,180)
    # polygon(bob,15,30)
    # square(bob,60)
    # circle(bob, 60)
    # arc(bob,80,180)
    # polyline
    # wait_for_user()

if __name__ == '__main__':
    main()
