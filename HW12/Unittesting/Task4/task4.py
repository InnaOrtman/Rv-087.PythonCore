import random

def guess_number(number, value):
    if value > number:
        return 2
    elif value < number:
        return 0
    else:
        return 1
