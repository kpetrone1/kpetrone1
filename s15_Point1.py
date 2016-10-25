class Point:
    """Represents a point in 2-D space.
    attributes: x, y
    """


my_point = Point()
print(my_point)

def print_point(p):
    """Print a Point object in human-readable format."""
    print('(%g, %g)' % (p.x, p.y))


def distance_between_points(p1, p2):
    """Computes the distance between two Point objects.
    p1: Point
    p2: Point
    returns: float
    """
    pass


class Rectangle:
    """Represents a rectangle. 
    attributes: width, height, corner.
    """


def find_center(rect):
    """Returns a Point at the center of a Rectangle.
    rect: Rectangle
    returns: new Point
    """
    p = Point()
    p.x = rect.corner.x + rect.width / 2.0
    p.y = rect.corner.y + rect.height / 2.0
    return p


def grow_rectangle(rect, dwidth, dheight):
    """Modifies the Rectangle by adding to its width and height.
    rect: Rectangle object.
    dwidth: change in width (can be negative).
    dheight: change in height (can be negative).
    """
    rect.width += dwidth
    rect.height += dheight


def main():
    my_point = Point()
    my_point.x = 3
    my_point.y = 4
    print('My point', end=' ')
    print_point(my_point)

    box = Rectangle()
    box.width = 100.0
    box.height = 200.0
    box.corner = Point()
    box.corner.x = 0.0
    box.corner.y = 0.0

    center = find_center(box)
    print('center', end=' ')
    print_point(center)

    print(box.width)
    print(box.height)
    print('grow')
    grow_rectangle(box, 50, 100)
    print(box.width)
    print(box.height)


# if __name__ == '__main__':
#     main()