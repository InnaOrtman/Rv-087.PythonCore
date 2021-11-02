print('Enter your numbers, expect 0')
print('To stop, just press enter')

positiveNumbers = 0
userNumbers = []

while True:
    try:
        userNumber = int(input('Enter your number \n'))

        if userNumber == 0:
            print('Your number can not be 0')
            break
        elif userNumber > 0:
            positiveNumbers += 1
            userNumbers.append(userNumber)
        else:
            userNumbers.append(userNumber)
    except:
        break

totalNumbers = len(userNumbers)
print('The percentage of positive numbers: ', positiveNumbers/totalNumbers * 100, '%', 'The percentage of negative numbers: ', 100-(positiveNumbers/totalNumbers * 100), '%')

