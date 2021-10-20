#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Task 1 (Python 2.7)
# Define variables a and b. Read values a and b from console and calculate:
#     a + b
#     a - b
#     a * b
#     a / b.
# Output obtained results.

def is_number(variable):
    count_dot = 0
    for i in range(len(variable)):
        if variable[i] != ".":
            try:
                int(variable[i])
            except ValueError:
                return False
        if variable[i] == ".":
            count_dot += 1
    if count_dot > 1:
        return False
    return True


def if_int_to_int(number):
    if number % 1 == 0:
        return int(number)
    return number


def main():
    a = raw_input(u"Enter value of variable a: ")
    b = raw_input(u"Enter value of variable b: ")

    if is_number(a) == True and is_number(b) == True:
        a = float(a)
        b = float(b)
        print u"a + b = {}".format(if_int_to_int(a + b))
        print u"a - b = {}".format(if_int_to_int(a - b))
        print u"a * b = {}".format(if_int_to_int(a * b))

        try:
            truediv = a / b
        except ZeroDivisionError:
            truediv = u"{0} / {1}: You can't division on 0".format(a, b)
        if not is_number(str(truediv)):
            print(truediv)
        else:
            print(u"a / b = {}".format(if_int_to_int(truediv)))
    else:
        print u"Variable a or b not is a number (a = {}, b = {})".format(a, b)


if __name__ == "__main__":
    main()
