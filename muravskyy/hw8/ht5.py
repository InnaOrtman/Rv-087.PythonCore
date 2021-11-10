def is_year_leap(year:int):
    if year > 1583:
        if year%4 != 0 or \
        (year%100 == 0 and year%400 != 0):
            return False
    return True