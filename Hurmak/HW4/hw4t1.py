year = int(input('Enter the year:'))
isLeap = ''
if year%4 == 0 and not year%100 == 0 or year%400 == 0:
    isLeap = 'leap'
else:
    isLeap = 'regular'

if year > 0:
    century = int((year-1)/100) + 1
    anno = 'AD'
else:
    century = abs(int(year/100) - 1)
    anno = 'BC'

print(f'{year} is {isLeap} year, {century} {anno}')




