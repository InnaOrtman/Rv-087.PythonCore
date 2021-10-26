import random
from datetime import datetime

number = random.randint(1, 100)
print(number)

for i in range (1, 11):
    guessed_number = int(input("Please enter your guess.\n"))
    if guessed_number == number:
        print(f"YOU ARE A WINNER! It took you {i} tries to find the number!")
        break
    elif guessed_number > number:
        print(f"Wrong, your number is bigger than one we chose. Attempts left: {10-i}")
    else:
        print(f"Wrong, your number is smaller than one we chose. Attempts left: {10-i}")
else:
    print(f"It took your {i} tries, but no luck. The number was {number}.")

