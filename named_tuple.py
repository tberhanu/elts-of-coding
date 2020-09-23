from collections import namedtuple
def foo():
    Point = namedtuple("Point", "x y")
    pt1 = Point(1.0, 5.0)
    pt2 = Point(2.5, 1.5)
    print("pt1: ", pt1)
    print("pt1.x :", pt1.x, pt1[0])
    print("pt2: ", pt2)
    print("pt2.y :", pt2.y, pt2[1])
    print("-------------------------")
    Point = namedtuple("Point", ("x", "y"))
    pt1 = Point(1.0, 5.0)
    pt2 = Point(2.5, 1.5)
    print("pt1: ", pt1)
    print("pt1.x :", pt1.x, pt1[0])
    print("pt2: ", pt2)
    print("pt2.y :", pt2.y, pt2[1])

foo()

