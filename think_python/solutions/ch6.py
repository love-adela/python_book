# Exercise 6-1

def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x += 1
    return x * y

def c(x, y, z):
    total = x + y + z
    square = b(total) ** 2
    return square

x = 1
y = x + 1
print(c(x, y + 3, x + y))


# Exercise 6-2

def ack(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0 :
        return ack(m-1, 1)
    elif m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))
    else:
        raise ValueError('Illegal Argument')

print(ack(3, 4)) # 125
print(ack(-1, -10)) # 'Error'

# Exercise 6-3
# palindrome.py 참고

# Exercise 6-4

def is_power(a, b):
    if(a == b): #base case a = b
            return True
    elif(a % b != 0):
            return False
    else:
            return is_power(a/b , b)

print(is_power(8,2))
print(is_power(9,2))


# Exercise 6-5

# 최대공약수
def gcd(a, b):
    a = int(a)
    b = int(b)
    if a > b:
        c = a - b
        gcd(b, c)
    elif a < b:
        c = b - a
        gcd(a, c)
    else:
        print(a)
		
gcd(252, 105)

# 유클리드
def euclidean(a,b):
    if (b == 0):
        return a
    else:
        return euclidean(b, a%b)

print(euclidean(105, 252))
