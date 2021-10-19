#!/usr/bin/env python3
# is_number
# if_int_to_int
# if_number_to_float


def is_number(variable: str) -> bool:
    count_dot = 0
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


def if_number_to_float(variable: str) -> [float, str]:
    if not is_number(variable):
        return variable
    return float(variable)


def if_int_to_int(number: [int, float]) -> [int, float]:
    if number % 1 == 0:
        return int(number)
    return number


def main():
    pass


if __name__ == "__main__":
    main()
