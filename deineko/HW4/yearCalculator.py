print('Enter a year')

year = int(input())
century = (year // 100) + 1 

print(century,'th century')

if year % 4 == 0:
    print('The year is intercalary')
else:
    print('The year isn\'t intercalary')

