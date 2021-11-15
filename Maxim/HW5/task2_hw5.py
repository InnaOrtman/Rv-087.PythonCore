# Task 2
# User enters ten natural numbers greater than 2.
# Count how many of them are numbers that are multiples of 5.

from mynum import is_positive_integer


i = 1
listNumbers = []
count = 0

while i < 11:
    number = input(f"Enter the number #{i}: ")

    if not is_positive_integer(number) or int(number) <= 2:
        print("You enter not a number or not a positive natural number\n"
              "or number less then 3")
        continue
    listNumbers.append(number)
    i += 1

for item in listNumbers:
    if int(item) % 5 == 0:
        count += 1

# print(listNumbers)
print(str(count) + " of numbers are multiples of 5")
