# Task 3
# Create a date function that takes 3 arguments - day, month and year.
# Return True if such a date is in our calendar, and False - otherwise.

from mynum import is_fraction_in_number
from mynum import is_number
from task5_hw8 import isLeapYear


def inputDate() -> []:
    global date_
    isDate = False
    while not isDate:
        date_ = [input("Enter the day: "),
                 input("Enter the month: "),
                 input("Enter the year (from -9999 to 9999):")]
        correct = True
        for i in range(len(date_)):
            if is_fraction_in_number(date_[i]):
                correct = False
                break
            if not is_number(date_[i]):
                correct = False
                break
            if date_[i] == "-0":
                date_[i] = "0"
            date_[i] = int(date_[i])

        if correct:
            if not -9999 <= date_[2] <= 9999:
                correct = False
            if date_[0] < 0 or date_[1] < 0:
                correct = False

        if not correct:
            print("You enter incorrect data")
            continue

        isDate = True
    return date_


def dateFunc(date: list) -> bool:
    dictYear = {1: 31,
                2: 28,  # if leap change 28 to 29
                3: 31,
                4: 30,
                5: 31,
                6: 30,
                7: 31,
                8: 31,
                9: 30,
                10: 31,
                11: 30,
                12: 31}

    day, month, year = date

    if year < 1583:
        if month in dictYear and day <= dictYear[month]:
            return True
        return False
    if month != 2:
        if month in dictYear and day <= dictYear[month]:
            return True
    elif month == 2:
        if isLeapYear(year):
            dictYear[month] = 29
        if day <= dictYear[month]:
            return True
    return False


print(dateFunc(inputDate()))
