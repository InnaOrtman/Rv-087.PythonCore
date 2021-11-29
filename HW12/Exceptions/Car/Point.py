import math
from Point_exceptions import *


class Point:
    def __init__(self, x: int = 0, y: int = 0):
        try:
            self.x = x
            self.y = y
            if self.x < 0 or self.y < 0:
                raise NegativeCoordsError
        except NegativeCoordsError as e:
            print(e.message)
        else:
            print("Coords are correct")


    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def distance_to(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    def __sub__(self, other):
        try:
            if self.x - other.x < 0 or self.y - other.y < 0:
                raise NegativeCoordsError
        except NegativeCoordsError as e:
            print(e.message)
        else:
            print("Such substraction is allowed")
            return Point(self.x - other.x, self.y - other.y)

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __ne__(self, other):
        return self.x != other.x and self.y != other.y