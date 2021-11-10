def is_year_leap(year:int):
    if year > 1583:
        if year%4 != 0 or \
        (year%100 == 0 and year%400 != 0):
            return False
    return True

def data(day, month, year) -> int:
    day_of_month = [31, 29, 31, 30, 31, \
    30, 31, 31, 30, 31, 30, 31]
    if is_year_leap(year) == False:
        day_of_month[1] = 28
    if month <= 12:
        if day <= day_of_month[month - 1]:
            return True
    return False

print(data(29,2,1900))