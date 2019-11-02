import sys
import os

def is_triangle(a,b,c):
    if (a + b > c) and (a + c > b) and (b + c > a):
        print("Yes")
    else:
        print("No")

def prompt():
    prompt = "Please enter side "
    for value in ['a', 'b', 'c']:
        new_prompt = prompt + value +': ' 
        my_input = float(input(new_prompt))   
        exec ("%s=%f" % (value, my_input))
    is_triangle(int(a),int(b),int(c))

def main():
    is_triangle(5,3,4)
    is_triangle(5,3,12)
    prompt()

if __name__ == '__main__':
    main()
