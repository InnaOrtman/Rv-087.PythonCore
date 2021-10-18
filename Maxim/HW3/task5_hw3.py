# Task 5
# Calculate the length of the hypotenuse on the two entered other
#   sides of the right triangle.

import sys
import os
import math

PACKAGE_PARENT = '..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(
    os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

from mynum import if_number_to_float

cathetusFirst = if_number_to_float(
    input("Enter a value of first cathetus: "))
cathetusSecond = if_number_to_float(
    input("Enter a value of second cathetus: "))


if not isinstance(cathetusFirst, float) or\
        not isinstance(cathetusSecond, float):
    print(f"One or both of values of cathetus not a number!\n"
          f"You enter such values:\n"
          f"First cathetus: {cathetusFirst}\n"
          f"Second cathetus: {cathetusSecond}")
else:
    hypotenuse = math.sqrt(cathetusFirst * cathetusFirst
                           + cathetusSecond * cathetusSecond)
    print("The length of the hypotenuse: ", hypotenuse)
