def dateFunction(day, month, year):
    longMonths = (1, 3, 5, 7, 8, 10, 12)
    shortMonths = (4, 6, 9, 11)
    if year <= 1582 or month > 12:
        return False
    elif day <= 29 and month == 2 and year % 4 == 0:
        return True
    elif day <= 28 and month == 2 and year % 4 != 0:
        return True 
    elif day <= 31 and month in longMonths:
        return True
    elif day <= 30 and month in shortMonths:
        return True
    else:
        return False

day = int(input('Enter a day: '))
month = int(input('Enter a month: '))
year = int(input('Enter a year: '))

print(dateFunction(day, month, year))
    