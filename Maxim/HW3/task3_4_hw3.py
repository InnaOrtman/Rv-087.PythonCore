# Task 3 & Task 4
# Task 3:
# Calculate the area and perimeter of the rectangle
#   for an entered width and height.
# + Square
# Task 4:
# Calculate the area and perimeter of the circle over an entered radius.
#
# TODO:
#   Make properties for the methods


import abc
import math


class AbstaractGeomFigure(abc.ABC):
    @abc.abstractmethod
    def area(self):
        """ Return area of geometric figure """
        pass

    @abc.abstractmethod
    def perimeter(self):
        """ Return perimeter of geometric figure """
        pass


class Rectangle(AbstaractGeomFigure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


class Circle(AbstaractGeomFigure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius * self.radius

    def perimeter(self):
        return 2 * self.radius * math.pi


rectangle = Rectangle(7, 5)
square = Square(5)
circle = Circle(6)

print("area of rectangle: ", rectangle.area())
print("perimeter of rectangle: ", rectangle.perimeter())
print()
print("area of rectangle: ", square.area())
print("perimeter of square: ", square.perimeter())
print()
print("area of circle: ", circle.area())
print("perimeter of circle: ", circle.perimeter())
