# Task 1
# The program generates a random integer from 0 to 100. The user must guess
# it in no more than 10 attempts. After each unsuccessful attempt, program
# says if the number entered by user more or less than required number. If the
# number is not guessed for 10 attempts, then display the guessed number.
"""
Цю гру я розробила для іншого свого курсу,
але для даного завдання я думаю вона теж підійде)))
"""

print ( "🙃🙃🙃Welcome to the Number Guessing Game!🙃🙃🙃\nI'm thinking of a number between 1 and 100." )
import random

x = random.randint ( 1, 100 )
print ( f"Pssst, the correct answer is {x}" )
y = int ( input ( "Choose a difficulty. Choose easy (1) or hard(2):" ) )

if y == 1:
    number_t = 10
elif y == 2:
    number_t = 5
else:
    print ( "Please, enter a valid number" )

print ( f"You have {number_t} attempts remaining to guess the number." )

should_continue = True
while should_continue:
    z = int ( input ( "Make a guess:" ) )
    if z > x:
        print ( "Too high." )
        number_t -= 1
        print ( "Guess again." )
        print ( f"You have {number_t} attempts remaining to guess the number." )
    if z < x:
        print ( "Too low." )
        number_t -= 1
        print ( "Guess again." )
        print ( f"You have {number_t} attempts remaining to guess the number." )
    if z == x:
        should_continue = False
        print ( f"🙃🙃🙃You got it! The answer was {x}.🙃🙃🙃" )
    if number_t == 0:
        should_continue = False
        print ( f"The answer was {x}." )
        print ( "😭😭You've run out of guesses, you lose.😭😭\n!!GOODBYE!!" )
