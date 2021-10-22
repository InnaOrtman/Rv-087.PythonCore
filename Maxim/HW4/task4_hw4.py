# Task 4
# Is it possible to place a round stage with radius R in a square hall
# of square S so that there is a passage was at least K from the wall
# to the stage?

import math
import parrPathApp
from mynum import is_number
from mynum import if_int_to_int


parrPathApp.run()


def main():
    radius = input("Enter the radius of circle: ")
    areaSquare = input("Enter the area \"S\" of square: ")
    passageK = input("Enter a value of passage \"K\" from the wall: ")

    if not is_number(radius) or \
            not is_number(areaSquare) or \
            not is_number(passageK):
        print(f"Some value is incorrect, you entered:\n"
              f"radius: {radius}\n"
              f"area of square \"S\": {areaSquare}\n"
              f"passage \"K\": {passageK}")
        return -1

    res = "possible"
    radius = float(radius)
    areaSquare = float(areaSquare)
    passageK = float(passageK)
    squareSide = math.sqrt(areaSquare)

    correctionK = squareSide - passageK
    if radius * 2 > correctionK:
        res = "impossible"

    radius = if_int_to_int(radius)
    areaSquare = if_int_to_int(areaSquare)
    passageK = if_int_to_int(passageK)

    print(f"It is {res} to place a round stage with:\n"
          f"radius \"{radius}\" in a square with\n"
          f"area \"{areaSquare}\" and passage {passageK}\"")


if __name__ == "__main__":
    main()
