def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


class Time:
    def __init__(self, hour=0, minute=0, second=0):
        self.hour = hour
        self.minute = minute
        self.second = second
        # attribute = parameter

    def __str__(self):
        return '%.2d: %.2d :%.2d' % (self.hour, self.minute, self.second)

    def __add__(self, other):
        if isinstance(other, Time):
            return self.add_time(other)
        else:
            return self.increment(other)
    
    def __radd__(self, other):
        return self.__add__(other)

    def add_time(self, other):
        seconds = self.time_to_int() + other.time_to_int()
        return int_to_time(seconds)

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)


    def print_time(self):
        print('%.2d: %.2d :%.2d' % (self.hour, self.minute, self.second))
    # TODO: versatile => polymorphism이해하고 다시 보자.
    
    def time_to_int(self) -> int: # pure function
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def is_after(self, other) -> bool:
        return self.time_to_int() > other.time_to_int()

start = Time(9, 45)
duration = Time(1, 35)
print(start + duration)
print('These are same because of __radd__ method')
print(start + 1337)
print(1337 + start)

t1 = Time(7, 43)
t2 = Time(7, 41)
t3 = Time(7, 37)
print(sum([t1, t2, t3]))

# Method takes instance as first argument.
# Subject : start -> 주체... method의 주어. (Subject <- Object) 
# Object : Time -> 객체 (대상)
# 관점이 start라는 객체
start.print_time()
# print(start.time_to_int())
end = start.increment(1337)
end.print_time()

print(start.is_after(end))

# If you provide one argument in class override first parameter.
# override : 덮어씀
time = Time(9)
time = Time(9, 45)
time.print_time()
print(time)

# Ex

class Point:
    def __init__(self, x=0, y=0): # Optional parameters
        self.x = x
        self.y = y

    def __str__(self):
        return '%d, %d' % (self.x, self.y)
        
    def __add__(self, other):
        if isinstance(other, Point):
            return Point(self.x + other.x, self.y + other.y)
        else:
            return Point(self.x + other[0], self.y + other[1])

p1 = Point(16, 85)
p2 = Point(3, -80)

print(p1 + p2)
print(p1 + (1,3))

# Polymorphic : 
# Functions that work with several types are called polymorphic.
# Polymorphism can facilitate code reuse.
# As long as the elements of s are hashable, this function also works for lists, tuples, and even dictionaries. So they can be used as keys in d.
def histogram(s) -> dict:
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

t = ['spam', 'egg', 'spam', 'spam', 'bacon', 'spam'] # list
print(histogram(t))

# d = {'spam': 4, 'egg': 1, 'bacon':1}
