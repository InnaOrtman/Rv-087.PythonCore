import math


P = 10
H = 30

print('Enter the sequence of numbers')

userNumbers = []
lessThanP = []
moreThanH = []

while True:
    try:
        userNumber = int(input('Enter your number \n'))

        if userNumber == P or userNumber == H:
            print('Your number can not be 10 or 30')
            break
        elif userNumber < P:
            lessThanP.append(userNumber)
            userNumbers.append(userNumber)
        elif userNumber > H:
            moreThanH.append(userNumber)
            userNumbers.append(userNumber)
    except:
        break

print('The list of your numbers: ', userNumbers)
print('The sum of numbers < P: ', sum(lessThanP))
print('The product of numbers > H: ', math.prod(moreThanH))
print('The number of numbers in the range of values from P to H', P-H)