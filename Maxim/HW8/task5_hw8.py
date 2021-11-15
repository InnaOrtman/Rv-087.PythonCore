# Task 5
# 	Create the function is_year_leap, that takes 1 argument - year,
# 	and returns True if the year is high, and False otherwise.

from mynum import is_number
from mynum import is_fraction_in_number


def inputYear() -> str:
    global year
    isYear = False
    while not isYear:
        year = input("Enter the year in the range from -9999 to 9999: ")

        if is_fraction_in_number(year):
            print("The year must be without fraction")
            continue

        if not is_number(year):
            print("The value isn't a number")
            continue

        if year == "-0":
            year = "0"

        year = int(year)

        if not -9999 <= year <= 9999:
            continue
        isYear = True
    return year


def isLeapYear(yearInp: int) -> bool:
    if yearInp % 4 != 0 or \
            yearInp % 100 == 0 and yearInp % 400 != 0:
        return False
    return True


if __name__ == "__main__":
    year_ = int(inputYear())
    if year_ > 1581:
        print(isLeapYear(year_))
    else:
        print(f"The Gregorian calendar was only adopted in 1582. To "
              f"say a leap year or not, it must be later than 1582.")
