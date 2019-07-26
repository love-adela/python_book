def find_partner(a):
    n = len(a)

    for i in range(1, n-1):
        for j in range(i+1, n):
            print(a[i], "-" , a[j])
name = ["Tom", "Jerry", "Mike"]
find_partner(name) #이 문장만으로 출력이 되는 이유?
print()

name2 = ["Tom", "Jerry", "Mike", "John"]
find_partner(name2)
print()