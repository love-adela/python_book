def findresult(a, x):
    n = len(a)
    result = []

    for i in range (0, n):
        if x == a[i]:
            result.append(i)

    return result


v = [17, 92, 18, 33, 58, 7, 33, 42]
print(findresult(v, 33))
print(findresult(v, 7))