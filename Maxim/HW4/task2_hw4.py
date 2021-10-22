# Task 2
# Depending on the user's choice, calculate the square of either a
# rectangle, or a triangle, or a circle.
# If a rectangle or triangle is selected, the lengths of the sides
# should be invited; is circle, its radius.

import parrPathApp
import task3_4_hw3 as figure
from mynum import is_number
from mynum import is_positive_natural
from mynum import if_int_to_int


parrPathApp.run()


def main():
    incorrMess = "You entered incorrect number"
    notNumMess = "You entered not a number"

    userChoise = input("Choose the area of what figure \
                       do you want to calculate\n"
                       "1 - Circle\n"
                       "2 - Rectangle\n"
                       "3 - Square\n"
                       "4 - Triangle\n"
                       "Yor choice is: ")

    if not is_positive_natural(userChoise):
        print(incorrMess)
        return -1

    userChoise = int(userChoise)

    if not 0 < userChoise < 5:
        print(incorrMess)
        return -1

    # Circle
    if userChoise == 1:
        radius = input("Enter the radius of the circle: ")
        if not is_number(radius):
            print(incorrMess)
            return -1
        radius = float(radius)
        circle = figure.Circle(radius)
        print(f"Area of circle: {if_int_to_int(circle.area())}")
        return 1

    # Rectangle
    if userChoise == 2:
        sides = []
        print("To calculate the area of rectangle you need to enter 2 sides")
        for i in range(1, 3):
            side = input(f"Enter the value of side #{i}: ")
            if not is_number(side):
                print(notNumMess)
                return -1
            sides.append(float(side))
        rectangle = figure.Rectangle(*sides)
        print(f"Area of rectangle: {if_int_to_int(rectangle.area())}")
        return 1

    # Square
    if userChoise == 3:
        print("To calculate the area of square you need to enter 1 side")
        side = input("Enter the side of square: ")
        if not is_number(side):
            print(notNumMess)
            return -1
        square = figure.Square(float(side))
        print(f"Area of square: {if_int_to_int(square.area())}")
        return 1

    # Triangle
    if userChoise == 4:
        sides = []
        print("To calculate the area of triangle you need to enter 3 sides")
        for i in range(1, 4):
            side = input(f"Enter the value of side #{i}: ")
            if not is_number(side):
                print(notNumMess)
                return -1
            sides.append(float(side))
        triangle = figure.TriangleThreeSides(*sides)
        print(f"Area of triangle: {if_int_to_int(triangle.area())}")
        return 1


if __name__ == "__main__":
    main()
