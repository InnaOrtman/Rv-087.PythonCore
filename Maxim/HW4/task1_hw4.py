# Task 1
# The YEAR is known. Determine whether this year is
# intercalary and to what century this year belongs.

import parrPathApp
from mynum import is_number
from mynum import is_fraction_in_number


parrPathApp.run()

yearInt = int()


def inputYear() -> [str, tuple]:
    year = input("Enter the year in the range from -9999 to 9999: ")

    if is_fraction_in_number(year):
        return "You can't enter a number with fraction", None

    if year == "-0":
        year = "0"

    if not is_number(year):
        return "You didn't enter a number", None

    global yearInt
    yearInt = int(year)

    if not -9999 <= yearInt <= 9999:
        return "You entered the year not in range from -9999 to 9999", None

    return year


def whatCent(year: str) -> [str, tuple]:
    lenYear = len(year)
    cent = "Century"
    centBC = "Century BC"

    if year[0:1] != "-":
        if 0 <= yearInt <= 100:
            return "1", cent
        elif lenYear == 3:
            if year[-2:] != "00":
                return int(year[:1]) + 1, cent
            else:
                return int(year[:1]), cent
        elif lenYear == 4:
            if year[-2:] != "00":
                return int(year[:2]) + 1, cent
            else:
                return int(year[:2]), cent
        else:
            return "Something wrong in block where year without '-'"
    elif year[0:1] == "-":
        if 0 > yearInt >= -100:
            return "1", centBC
        elif lenYear == 4:
            if year[-2:] != "00":
                return int(year[1:2]) + 1, centBC
            else:
                return int(year[1:2]), centBC
        elif lenYear == 5:
            if str(year)[-2:] != "00":
                return int(year[1:3]) + 1, centBC
            else:
                return int(year[1:3]), centBC
        else:
            return "Something wrong in block where year without '-'"
    else:
        return "Something went wrong..."


def isLeapYear(year: int) -> bool:
    if year % 4 != 0 or \
            year % 100 == 0 and year % 400 != 0:
        return False
    return True


def main():
    year = inputYear()
    if isinstance(year, tuple):
        print(year[0])
        return
    century = whatCent(year)
    if isinstance(century, str):
        print(century)
    else:
        if yearInt < 1582:
            print(f"The Gregorian calendar was only adopted in 1582. To "
                  f"say a leap year or not, it must be later than 1582.")
        else:
            if isLeapYear(yearInt):
                print(f"The year {yearInt} is a leap, 366 days")
            else:
                print(f"The year {yearInt} isn't a leap, 365 days")
    print(century[0], century[1])


if __name__ == "__main__":
    main()
