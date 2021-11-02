import random

number = random.randint(1, 100)

for i in range (1, 11):
    guessed_number = int(input("Please enter your guess.\n"))

    if guessed_number > number:
        print(f"Wrong, your number is bigger than one we chose. Attempts left: {10-i}")
    elif guessed_number < number:
        print(f"Wrong, your number is smaller than one we chose. Attempts left: {10-i}")
    else:
        print(f"YOU ARE A WINNER! It took you {i} tries to find the number!")
        break
else:
    print(f"It took your {i} tries, but no luck. The number was {number}.")

