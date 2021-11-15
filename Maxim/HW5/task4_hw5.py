# Task 4
# Display a "rectangle" formed of two types of characters.
# The outline of the rectangle should consist of one character,
# and "fill" - of another.

from mynum import is_positive_integer

side1 = input("Enter value of first side: ")
side2 = input("Enter value of second side: ")

if not is_positive_integer(side1) and \
        not is_positive_integer(side2):
    print("You entered not a correct number(s)")
else:
    side1, side2 = int(side1), int(side2)

    for i in range(1, side2 + 1):
        for j in range(1, side1 + 1):
            if (i == 1 or i == side2
                    or j == 1 or j == side1):
                print("*", end="")
            else:
                print(".", end="")
        print()
