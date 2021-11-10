#!/usr/bin/env python3
# checkInput

from mynum import is_positive_integer


def checkInputPosNat(lst: list) -> bool:
    for i in range(len(lst)):
        if not is_positive_integer(lst[i]):
            print("You entered incorrect data")
            return False
    return True
