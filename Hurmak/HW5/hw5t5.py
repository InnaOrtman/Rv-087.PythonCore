p = 5
h = 20
num = 0
inTheMiddle = 0
belowP = 0
overH = 1
while num != p and num != h:
    num = int(input('Enter a number:'))
    if p <= num <= h:
        inTheMiddle += 1
    elif num < p:
        belowP += num
    else:
        overH *= num
print(f'{belowP} - sum of numbers less than P .'
      f'\n{overH} - product of numbers greater than H.'
      f'\n{inTheMiddle} - number of numbers in range from P to H')
