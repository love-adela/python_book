def make_foo(a):
    def inner2():
        a += 1
        return a
    return inner2

print(make_foo(4))
