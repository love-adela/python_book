def find_square_max(n) :
    s = 0
    for i in range (1, n+1):
        s = s+ i*i
    return s
print(find_square_max(10))