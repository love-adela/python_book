import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

blank = Point(3.0, 4.0)
another_blank = Point(15.0, 16.0)
 
def print_point(p):
    return '(%g, %g)' % (p.x, p.y)
# CAUTION: 외부의 attribute를 참조하는 형태 말고 method를 참조하는 형태가 좋다.-> encapsulation
print(print_point(blank))

def distance_between_points(p1, p2):
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)   
print(distance_between_points(blank, another_blank))

def distance_between_points(p1, p2):
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)
print(distance_between_points(blank, another_blank))

def distance_between_points(p1, p2):
    return math.sqrt((p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2)
print(distance_between_points(blank, another_blank))
