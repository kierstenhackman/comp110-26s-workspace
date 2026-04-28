from __future__ import annotations

"""Challenge Questions!"""

__author__ = "730739966"


class Point:
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        return Point(self.x * factor, self.y * factor)
