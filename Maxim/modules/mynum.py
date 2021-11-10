#!/usr/bin/env python3
# is_number
# is_positive_number
# is_fraction_in_number
# is_positive_integer
# if_number_to_float
# if_int_to_int


def is_number(variable: str) -> bool:
    if variable == ".":
        return False
    count_dot = 0
    if variable[-1:] == ".":
        count_dot += 1
    if variable[0:1] == "-":
        variable = variable[1:]
    for i in range(len(variable)):
        if count_dot > 1:
            return False
        if variable[i] == ".":
            count_dot += 1
            continue
        try:
            int(variable[i])
        except ValueError:
            return False
    return True


def is_positive_number(variable: str) -> bool:
    if len(variable) == 2:
        if variable[0:1] == "-" and variable[1:] == "0":
            return True
        elif variable[0:1] != "-":
            return True
    elif variable[0:1] == "-":
        return False
    else:
        return True
    return False
    
    
def is_fraction_in_number(variable: str) -> bool:
    for i in range(len(variable)):
        if variable[i] == ".":
            return True
    return False


def is_positive_integer(variable: str) -> bool:
    if variable[0:1] == "-":
        return False
    for i in range(len(variable)):
        if variable[i] == ".":
            return False
        try:
            int(variable[i])
        except ValueError:
            return False
    return True


def if_number_to_float(variable: str) -> [float, str]:
    if not is_number(variable):
        return variable
    return float(variable)


def if_int_to_int(number: [int, float]) -> [int, float]:
    if number % 1 == 0:
        return int(number)
    return number
