from polygon import circle, arc
import turtle

def fdlt(t, n, angle=90):
    t.fd(n)
    t.lt(angle)

def fdbk(t, n):
    t.fd(n)
    t.bk(n)

def skip(t, n):
    t.pu()
    t.fd(n)
    t.pd()

def stump(t, n, angle=90):
    t.lt(angle)
    t.fd(n)
    t.rt(angle)

def hollow(t, n):
    t.lt()
    skip(t, n)
    t.rt()

def post(t, n):
    t.lt(n)
    fdbk(t, n)
    t.rt(n)

def beam(t, n, height):
    hollow(t, n*height)
    fdbk(t, n)
    hollow(t, -n*height)


def hangman(t, n, height):
    stump(t, n * height)
    fdbk(t, n)
    t.lt(n)
    t.bk(n*height)
    t.rt(n)

def diagonal(t, x, y):
    from math import atan2, sqrt, pi
    angle = atan2(y, x) * 180 / pi
    dist = sqrt(x**2 + y**2)
    t.lt(angle)
    fdbk(t, dist)
    t.rt(angle)

def vshape(t, n, height):
    diagonal(t, -n/2, height*n)
    diagonal(t, n/2, height*n)

def bump(t, n, height):
    stump(t, n*height)
    arc(t, n/2.0, 180)
    t.lt()
    fdlt(t, n*height+n)

def draw_a(t, n):
    diagonal(t, n/2, 2*n)
    beam(t, n, 1)
    skip(t, n)
    diagonal(t, -n/2, 2*n)

def draw_b(t, n):
    bump(t, n, 1)
    bump(t, n, 0)
    skip(t, n/2)

def draw_c(t, n):
    hangman(t, n, 2)
    t.fd(n)

def draw_d(t, n):
    bump(t, 2*n, 0)
    skip(t, n)

def draw_ef(t, n):
    hangman(t, n, 2)
    hangman(t, n, 1)

def draw_e(t, n):
    draw_ef(t, n)
    t.fd(n)

def draw_f(t, n):
    draw_ef(t, n)
    skip(t, n)

def draw_g(t, n):
    hangman(t, n, 2)
    t.fd(n/2)
    beam(t, n/2, 2)
    t.fd(n/2)
    post(t, n)

def draw_h(t, n):
    post(t, 2*n)
    hangman(t, n, 1)
    skip(t, n)
    post(t, 2*n)

def draw_i(t, n):
    beam(t, n, 2)
    fd(t, n/2)
    post(t, 2*n)
    fd(t, n/2)

def draw_j(t, n):
    beam(t, n, 2)
    arc(t, n/2, 90)
    t.fd(3*n/2)
    skip(t, -2*n)
    t.rt()
    skip(t, n/2)

def draw_k(t, n):
    post(t, 2*n)
    stump(t, n, 180)
    vshape(t, 2*n, 0.5)
    fdlt(t, n)
    skip(t, n)

def draw_l(t, n):
    post(t, 2*n)
    t.fd(n)

def draw_n(t, n):
    post(t, 2*n)
    skip(t, n)
    diagonal(t, -n, 2*n)
    post(t, 2*n)

def draw_m(t, n):
    post(t, 2*n)
    draw_v(t, n)
    post(t, 2*n)

def draw_o(t, n):
    skip(t, n)
    circle(t, n)
    skip(t, n)

def draw_p(t, n):
    bump(t, n, 1)
    skip(t, n/2)

def draw_q(t, n):
    draw_o(t, n)
    diagonal(t, -n/2, n)

def draw_r(t, n):
    draw_p(t, n)
    diagonal(t, -n/2, n)

def draw_s(t, n):
    t.fd(n/2)
    t.arc(n/2, 180)
    t.arc(n/2, -180)
    fdlt(t, n/2, -90)
    skip(t, 2*n)
    t.lt()

def draw_t(t, n):
    beam(t, n, 2)
    skip(t, n/2)
    post(t, 2*n)
    skip(t, n/2)

def draw_u(t, n):
    post(t, 2*n)
    t.fd(n)
    post(t, 2*n)

def draw_v(t, n):
    skip(t, n/2)
    vshape(t, n, 2)
    skip(t, n/2)

def draw_w(t, n):
    draw_v(t, n)
    draw_v(t, n)

def draw_x(t, n):
    diagonal(t, n, 2*n)
    skip(t, n)
    diagonal(t, -n, 2*n)

def draw_v(t, n):
    skip(t, n/2)
    diagonal(t, -n/2, 2*n)
    diagonal(t, n/2, 2*n)
    skip(t, n/2)

def draw_y(t, n):
    skip(t, n/2)
    stump(t, n)
    vshape(t, n, 1)
    t.rt()
    fdlt(t, n)
    skip(t, n/2)

def draw_z(t, n):
    beam(t, n, 2)
    diagonal(t, n, 2*n)
    t.fd(t, n)

def draw_(t, n):
    skip(t, n)

if __name__ == '__main__':

    size = 20
    bob = turtle.Turtle()

    for f in [draw_h, draw_e, draw_l, draw_l, draw_o]:
        f(bob, size)
        skip(bob, size)
input()
