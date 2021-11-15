# Task 1
# Create an arithmetic function that takes 3 arguments: the first 2 are
# numbers, the third is the operation to be performed on them. If the
# third argument is +, add them; if -, then subtract; * - multiply; /
# - divide (first to second). In other cases, return the
# "Unknown operation" line.

from mynum import is_number
from mynum import if_int_to_int


def arithmetic(num1: [int, float],
               num2: [int, float],
               operation: str) -> [int, float]:
    posOperation = ("+", "-", "*", "/")
    if operation not in posOperation:
        return "Unknown operation"
    if is_number(num1) and is_number(num2):
        num1, num2 = float(num1), float(num2)
        if operation == posOperation[0]:
            return if_int_to_int(num1 + num2)
        elif operation == posOperation[1]:
            return if_int_to_int(num1 - num2)
        elif operation == posOperation[2]:
            return if_int_to_int(num1 * num2)
        elif operation == posOperation[3]:
            if num2 == 0:
                return "You can't divide on 0"
            return if_int_to_int(num1 / num2)
    else:
        return "first or second value is not number"


# print(arithmetic("6", "2", "+"))
# print(arithmetic("6", "2", "-"))
# print(arithmetic("6", "2", "*"))
# print(arithmetic("6", "2", "/"))
# print(arithmetic("6", "2", "="))
# print(arithmetic("5.2", "2.", "+"))
# print(arithmetic("6.2", "2", "-"))
# print(arithmetic("6", "2.32", "*"))
# print(arithmetic("6", "0", "/"))
print(arithmetic(input("Enter first value: "),
                 input("Enter second value: "),
                 input("Enter what operation: ")))
