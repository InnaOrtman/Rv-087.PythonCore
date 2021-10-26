# Task 6*
# The number of a place in the reserved carriage is given.
# Determine which place it is: top or bottom, compartment or side.

from mynum import is_positive_natural
from mynum import if_int_to_int


def main():
    number = input("Enter number of place: ")
    if not is_positive_natural(number):
        print("You entered not a correct number!")
        return -1

    number = float(number)

    if 0 < number < 55:
        inSide = "inside"
        bottom = "bottom"

        if number > 36:
            inSide = "outside"
        if number % 2 == 0:
            bottom = "top"

        print(f"The place {if_int_to_int(number)} is {inSide} "
              f"and it is in the {bottom}")
    else:
        print("There is no such place in the carriage")


if __name__ == "__main__":
    main()
