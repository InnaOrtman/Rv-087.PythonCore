# Task 1
# The program generates a random integer from 0 to 100.
# The user must guess it in no more than 10 attempts.
# After each unsuccessful attempt, program says if the number entered
# by user more or less than required number. If the number is not
# guessed for 10 attempts, then display the guessed number.

import random
from mynum import is_positive_integer


hiddenNumber = random.randrange(0, 101)
i = 1
win = False

print("Guess the hidden number from 0 to 100. You have 10 attempts.")
while i < 11:
    guess = input(f"Enter the number. Attempt {i}/10: ")

    if not is_positive_integer(guess):
        print("You enter not a number. You attempt won't be count.")
        continue
    elif int(guess) != hiddenNumber:
        if int(guess) > hiddenNumber:
            print("The number is less")
        else:
            print("The number is more")
        i += 1
    else:
        win = True
        break

if not win:
    print(f"You lost the game. The hidden number was {hiddenNumber}")
else:
    print(f"You won! The hidden number was {hiddenNumber}")
