import random

guessedNum = random.randint(0, 101)
guessed = False
print(guessedNum)
for i in range(10):
    tryNum = int(input('Enter guessed number: '))
    if tryNum < guessedNum:
        print('Entered number is less than guessed Number')
    elif tryNum > guessedNum:
        print('Entered number is greater than guessed Number')
    else:
        print('You guessed it')
        break
