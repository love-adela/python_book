# Exercise 3-1

def right_justify(s:str)->None:
    print(' ' * (70 - len(s)) + s)

print('')
right_justify('monty')

# Exercise 3-2

def do_twice(func, arg:str):
    func(arg)
    func(arg)

def print_twice(arg:str):
    print(arg)
    print(arg)

print('')
do_twice(print_twice, 'spam')

def do_four(func, arg:str):
    do_twice(func, arg)
    do_twice(func, arg)

print('')
do_four(print_twice, 'spam')


# Exercise 3-3

def do_twice(f):
    f()
    f()

def do_four(f):
    do_twice(f)
    do_twice(f)

def print_beam():
    print('+ - - - -', end='')

def print_post():
    print('|        ', end='')

def print_beams():
    do_twice(print_beam)
    print('+')

def print_posts():
    do_twice(print_post)
    print('|')

def print_row():
    print_beams()
    do_twice(print_posts)

def print_grid():
    do_twice(print_row)
    print_beams()

print_grid()
