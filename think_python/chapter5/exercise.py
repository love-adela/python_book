import time
import math

# Exercise 5-1
print('---------Exercise 5-1-----------')
def get_time():
    epoch = time.time()
    seconds_in_a_day = 24 * 60 * 60
    seconds_in_an_hour = 60 * 60
    seconds_in_a_minute = 60

    days = epoch // seconds_in_a_day
    hours = (epoch % seconds_in_a_day) // seconds_in_an_hour + 8
    minutes = (epoch % seconds_in_a_day) % seconds_in_an_hour // seconds_in_a_minute
    seconds = (epoch % seconds_in_a_day) % seconds_in_an_hour % seconds_in_a_minute
    print('Current time is %d: %d: %d' % (hours, minutes, seconds)) 
    print('Number of days since the epoch is %d' % (days))

get_time()

# Test
# TODO : python time모듈을 써서 자동으로 계산되게 짜보자.

# Exercise 5-2
print('---------Exercise 5-2-----------')
def check_fermat(n):
    if pow(a, n) + pow(b, n) == pow(c, n):
        print('Holy smikes, Fermat was wrong!')
    else:
        print("No, that doesn't work")

def prompt():
    print('2보다 큰 수를 입력하세요.')
    n = int(input())
    
    if n <= 2:
        print('2보다 큰 수여야 합니다.')
        prompt()
    else:
        check_fermat(n)

a = int(input('a를 입력하세요'))
b = int(input('b를 입력하세요'))
c = int(input('c를 입력하세요'))

prompt()

# Exercise 5-3
print('---------Exercise 5-3-----------')
def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        print('Yes')
    else:
        print('No')

def prompt():
    a = input('a를 입력하세요')
    b = input('b를 입력하세요')
    c = input('c를 입력하세요')

    return is_triangle(a, b, c)

prompt()
