def find_pair(a):
    n = len(a)


    for i in range (0, n-1):
        for j in range (i+1, n):
            print(a[i], "-", a[j])

pair=["Tom", "Jerry", "Mike"]
print(find_pair(pair))