from CQs.cq03.point import Point

"""Testing Challenge Questions!"""

__author__ = "730739966"

"""Creating a Point."""
a: Point = Point(3.0, 4.0)

"""Testing scale_by."""
print(a.x, a.y)  # before
a.scale_by(4)  # factor
print(a.x, a.y)  # after

"""Testing scale."""
new_point = a.scale(3)  # factor
print(a.x, a.y)  # before
print(new_point.x, new_point.y)  # after
