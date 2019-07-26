def gcd(a,b):
    if b == 0:
        return a
    return gcb(b, a%b)
print(gcd(1,5))
print(gcd(3,6))
print(gcd(60, 24))
print(gcd(81, 27))