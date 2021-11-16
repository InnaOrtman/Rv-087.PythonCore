def isLeapYear(year):
    if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0:
        return True
    else:
        return False


def checkDate(day, month, year):
    check = False
    daysInMonth = {(4, 6, 9, 11): 30, (1, 3, 5, 7, 8, 10, 12): 31}
    if not isLeapYear(year):
        daysInMonth[(2,)] = 28
    else:
        daysInMonth[(2,)] = 29
    for i, j in daysInMonth.items():
        if month in i and 0 < day <= j:
            check = True
    return check


print(checkDate(29, 2, 1900))
