def samename(a):
    name_dic = {
        39: "Justin",
        14: "JoHn",
        67: "Mike",
        105: "Summer"
    }
    if a in name_dic:
        return name_dic[a]
    else:
        return "?"

    }

print(samename(39))
print(samename(40))


a, b = (1, 2)

c, d = [1, 2]

