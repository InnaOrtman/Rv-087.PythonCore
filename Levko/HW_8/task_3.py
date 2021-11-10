# task_3

import datetime
day = int(input("Enter the day, please: "))
month = int(input("Enter month, please: "))
year = int(input("Enter year, please: "))


def date(day, month, year):
    date_1 = True
    try:
        datetime.datetime(year, month, day)
    except ValueError:
        date_1 = False
    if date_1:
        print("Input date is valid!")
    else:
        print("Input date is not valid!")

date(day, month, year)
