def findstudentno(s_no, s_name, find_no):
    n = len(s_no)

    for i in range(0, n):
        if find_no == s_no[i]:
            return s_name[i]
    return "?"



s_no = [39, 14, 67, 105]
s_name =["Justin", "John", "Mike", "Summer"]
print(findstudentno(s_no, s_name, 105))
print(findstudentno(s_no, s_name, 14))
print(findstudentno(s_no, s_name, 1))