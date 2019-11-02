import math
import copy

class Point: # header
    """Represents a point in 2-D space.""" # body
    def __init__(self, x, y):
        self.x = x
        self.y = y

blank = Point(3.0, 4.0)
print(f'blank 메모리상 주소는 {blank}')

class Rectangle:
    """Represents a rectangle.

    attributes: width, height, corner.
    """
    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner


def print_point(p: Point):
    print('중점 : (%g, %g)' % (p.x, p.y)) #CAUTION: 외부의 attribute를 참조하는 형태 말고 method를 참조하는 형태가 좋다.-> encapsulation    

box = Rectangle(6, 8, Point(0, 0))
print(f'직사각형의 폭과 넓이 :({box.width}, {box.height})')


def find_center(rect: Rectangle) -> Point:    
    p = Point(rect.corner.x + rect.width / 2 , rect.corner.y + rect.height / 2)
    return p

center = find_center(box)
print_point(center)

print('========================================')

def get_two_points(rect: Rectangle) -> tuple:
    p = Point(rect.corner.x, rect.corner.y + rect.height)
    q = Point(rect.corner.x + rect.width, rect.corner.y)
    return (p, q) 

def distance_between_points(p: Point, q:Point) -> float:
    return math.sqrt((q.x - p.x) ** 2 + (q.y - p.y) ** 2)

def print_two_points_and_distance(rect: Rectangle) -> tuple:
    (p, q) = get_two_points(rect)
    distance = distance_between_points(p, q)
    print(f'({p.x}, {p.y}), ({q.x}, {q.y}) 사이의 거리: {distance}') 

print_two_points_and_distance(box)


print('========================================')

def grow_rectangle(rect: Rectangle, dwidth:int, dheight:int) -> tuple:
    rect.width += dwidth
    rect.height += dheight
    return rect.width, rect.height

print(f'직사각형의 폭과 높이 : ({box.width}, {box.height})')
print(f'바뀐 직사각형의 폭과 높이: {grow_rectangle(box, 3, 4)}')


def move_rectangle(rect: Rectangle, dx:int, dy:int) -> Rectangle:
    """ This function should change the location of the rectangle by adding dx to the x coordinate of corner and adding dy to the y coordinate of corner.
    """
    rect.corner.x += dx
    rect.corner.y += dy
    return rect

move_rectangle(box, 1, -1)
print(f"좌표이동한 corner의 좌표 : {(box.corner.x, box.corner.y)}")

print('========================================')

p1 = Point(3.0, 4.0)
p1.x = 3.0
p1.y = 4.0

p2 = copy.copy(p1)
print_point(p1)
print_point(p2)

print(p1 is p2)
print(p1 == p2)

box2 = copy.copy(box)
print(box2 is box)
print(box2.corner is box.corner)

# shallow copy : 완전 값을 그대로 복사 (단 embedded objects는 복사하지 않는다.)
# deep copy : reference인지 확인(primitive인지 확인)하고 embedded object에 대해 재귀적으로 deep copy를 한다. 새로 만들어진 reference 값을 복사한다.

box3 = copy.deepcopy(box)
print(box3 is box)
print(box3.corner is box.corner)

def move_rectangle_make_new_rectangle():
    pass

