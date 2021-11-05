# Task 1
# Fill in one list with random numbers, another with numbers entered
# from the keyboard, and write the sums of the corresponding elements
# of the first two lists in the third one. Display the contents of the
# lists on the screen.

import random

from mynum import is_number


lenLists = random.randrange(3, 10)
lenListCopy = lenLists
# print("lenLists - ", lenLists)
list1 = [round(random.uniform(0, 100), 2) for _ in range(lenLists)]
list2, list3 = [], []

count = 1
while lenLists:
    num = input(f"Enter a number # {count}/{lenListCopy}: ")
    if not is_number(num):
        print("You entered incorrect data")
    else:
        list2.append(float(num))
        lenLists -= 1
        count += 1

list3 = [x+y for x, y in zip(list1, list2)]

print(list1)
print(list2)
print(list3)
