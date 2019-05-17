class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Rectangle:
    """Represents a rectangle.

    attributes: width, height, corner.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

box = Rectangle(100.0, 200.0)
box.corner = Point(0.0, 0.0)

def find_center(rect):
    p = Point()
    p.x = rect.corner.x + rect.width / 2
    p.y = rect.corner.y + rect.height / 2
    return p

center = find_center(box)
print(print_point(center))
