print('Enter a number')
number = int(input()) #55
numberToStr = str(number) #'55'
numberLength = len(numberToStr) #2


if number == 0:
    evenOrUneven = ''
elif number % 2 == 0:
    evenOrUneven = "even"
else:
    evenOrUneven = 'uneven'

if number > 0:
    posOrNeg = 'positive'
elif number < 0:
    posOrNeg = 'negative'
    numberLength = numberLength - 1
else:
    number = ''
    posOrNeg = '0'

print('The number', number, 'is', posOrNeg, evenOrUneven, 'and', numberLength, '-digit')