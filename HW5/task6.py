positive = 0
negative = 0
number = 0

while number != 0:
    number = int(input("Please enter number.\n"))
    if number > 0:
        positive += 1
    else:
        negative += 1

total = positive + negative
print(f"There are {total} numbers entered, {positive / total * 100}% are positive, {negative / total * 100}% are negative.")