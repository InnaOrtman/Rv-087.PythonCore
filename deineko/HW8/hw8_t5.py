def isYearLip(year):
    if year < 1582:
        print('Enter the year starting from 1582')
    elif year%4 == 0:
        return True
    else:
        return False

year = int(input('Enter a year: '))
print(isYearLip(year))