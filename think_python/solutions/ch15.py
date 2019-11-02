class Point(object):
    """Represents a point in 2-D space."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

def print_point(p:Point):
    print('(%g, %g)' % (p.x, p.y))

class Rectangle(object):
    """Represents a rectangle. 
    attributes: width, height, corner.
    """
    def __init__(self, width, height, corner):
        self.width = width
        self.height = height
        self.corner = corner

def find_center(rect:Rectangle)->Point:
    """Returns a Point at the center of a Rectangle."""
    p = Point()
    p.x = rect.corner.x + rect.width/2.0
    p.y = rect.corner.y + rect.height/2.0
    return p

def grow_rectangle(rect:Rectangle, dwith:int, dheight:int)->tuple:
    """Modify the Rectangle by adding to its width and height."""
    rect.width += dwidth
    rect.height += dheight
    return rect.width, rect.height

def main():
    blank = Point(3.0, 4.0)
    print('메모리상 blank 주소는')
    print_point(blank)

    box = Rectangle(100, 200, Point(0, 0))

    center = find_center(box)
    print('center')
    print_point(center)

    print(box_width)
    print(box_height)
    print('grow')
    grow_rectangle(box, 50, 100)
    print(box.width)
    print(box.height)

if __name__ == '__main__':
    main()
