# Task 5
# Given the number P and the number H.
# The user enters a sequence of numbers.
# Determine: the sum of those numbers that are less than P;
# product of numbers greater than H; the number of numbers
# in the range of values from P to H. When entering a number
# equal to P or H, stop the calculation and display the result.


from mynum import is_number
from mynum import if_int_to_int


quit_ = False
p, h = "", ""

while not quit_:
    p = input("Enter the number \"P\": ")
    h = input("Enter the number \"H\": ")
    if not is_number(p) or not is_number(h):
        print("You entered incorrect data")
    else:
        quit_ = True

listNumbers = []
count = 1

while True:
    num = input(f"Enter the number #{count}: ")
    if not is_number(num):
        print("You entered incorrect data")
    elif p == num or h == num:
        break
    else:
        listNumbers.append(float(num))
        count += 1

if not listNumbers:
    print("The list of numbers is empty")
else:
    sumNum = 0.0
    mulNum = 1.0
    count = 0
    p = float(p)
    h = float(h)

    for i in range(len(listNumbers)):
        if listNumbers[i] < p:
            sumNum += listNumbers[i]
        elif p < listNumbers[i] < h:
            count += 1
        else:
            mulNum *= listNumbers[i]

    sumNum = if_int_to_int(sumNum)
    mulNum = if_int_to_int(mulNum)
    if mulNum == 1:
        mulNum = 0

    print(listNumbers)
    print(f"sum of numbers before \"P ({p})\": {sumNum}")
    print(f"quantity of numbers between \"P ({p})\" and \"H ({h})\": {count}")
    print(f"The result of multiplying the numbers following after "
          f"\"H ({h})\": {mulNum}")
