# task_5
# Given the number P and the number H. The user enters a sequence of
# numbers. Determine: the sum of those numbers that are less than P; product
# of numbers greater than H; the number of numbers in the range of values
# from P to H. When entering a number equal to P or H, stop the calculation and
# display the result.
import math

P = 11
H = 22
print(f"Given the number {P} and the number {H}")
print("The user enters a sequence of numbers")
print(f"!!!Enter {P} or {H} if you want to finish and find out the result!!!")
list1 = []
list2 = []
list3 = []
list4 = []
a = True

while True:
    number = int(input("Enter the number: "))
    list4.append(number)
    if number < P:
        list1.append(number)
    elif number > H:
        list2.append(number)
    elif H > number > P:
        list3.append(number)
    elif number == P or number == H:
        del list4[-1]
        print(f"Your inputs : {list4}")
        break

print(f"The sum of those numbers that are less than {P}: {sum(list1)}")
print(f"The product of numbers greater than {H}: {math.prod(list2)}")
print(f"The number of numbers in the range of value from {P} to {H}: {len(list3)}")
