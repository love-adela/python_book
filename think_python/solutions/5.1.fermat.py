import sys
import os
import math

def check_fermat(a, b, c, n):
    left_side = pow(a, n) + pow(b, n)
    right_side = pow(c, n)
    if (n > 2) and (left_side == right_side):
        print("Holy Smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")


def prompt():
    prompt = "Please enter "
    for value in ['a', 'b', 'c', 'n']:
        new_prompt = prompt + value + '\n'  
        my_input = input(new_prompt)  
        float_input = float(my_input)  
        exec ("%s=%f" % (value, float_input))
    check_fermat(a, b, c, n)


def main():
    prompt()


if __name__ == '__main__':
    main()
