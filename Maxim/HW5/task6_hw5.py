# Task 6
# For user-entered numbers, determine the percentage of positive
# and negative numbers. When entering the number 0, finish the job.

from mynum import is_number
from mynum import if_number_to_float


quite_ = False
listNumbers = []

while not quite_:
    number = input("Enter a number: ")
    number = if_number_to_float(number)

    if not is_number(str(number)):
        print("You entered not a number")
    elif number == 0.0:
        quite_ = True
    else:
        listNumbers.append(number)

lenListNum = len(listNumbers)
count = 0
for i in range(lenListNum):
    if listNumbers[i] < 0:
        count += 1

percentWithMinus = count * 100 / lenListNum
percentWithoutMinus = 100 - percentWithMinus

# print(listNumbers)
print(f"100% - {lenListNum} numbers")
print(f"percent of negative numbers: {percentWithMinus}")
print(f"percent of positive numbers: {percentWithoutMinus}")
