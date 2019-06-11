import math

# Exercise 7-1
print('==========Exercise 7-1==========')
def mysqrt(a):
    epsilon = 0.00000000001
    x = 3.0 
    while True:
        y = (x + a / x) / 2
        if abs(y - x) < epsilon:
            return y 
            break
        x = y
    return(x)

# Test
def test_square_root(a):
    print('a  mysqrt(a)  math.sqrt(a) diff')
    print('-  ---------  -----------  ----')

    while a < 10.0:
        diff = abs(mysqrt(a) - math.sqrt(a))
        print(f'{a} {mysqrt(a):.12}  {math.sqrt(a):.12} {diff}')
        a += 1.0

test_square_root(1.0)

# Exercise 7-2
print('==========Exercise 7-2==========')
def eval_loop():
    while True:
        input_word = input()
        try:
            print(eval(input_word)) 
        except(NameError, SyntaxError):
            if input_word == 'done':
                break
            else:
                print(input_word)

eval_loop()

# Exercise 7-3
print('==========Exercise 7-3==========')
def estimate_pi():
    
    summation = 0
    k = 0
    factor = 2 * math.sqrt(2) / 9801
    while True:
        numerator = math.factorial(4*k) * (1103 + 26390 * k)
        denominator = math.pow(math.factorial(k), 4) * (math.pow(396, 4 * k))
        term = factor * numerator / denominator
        summation += term

        if abs(term) < math.pow(10, -15):
            break
        k += 1

    return 1 / summation

print(estimate_pi())
