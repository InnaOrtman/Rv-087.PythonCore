# Task 1
# Fill in one list with random numbers, another with numbers entered
# from the keyboard, and write the sums of the corresponding elements
# of the first two lists in the third one. Display the contents of the
# lists on the screen.

import random
from itertools import zip_longest

from mynum import is_number


lenLists = random.randrange(3, 10)
# print("lenLists - ", lenLists)
list1 = [round(random.uniform(0, 100), 2) for _ in range(lenLists)]
list2, list3 = [], []
quit_ = False

count = 1
while not quit_:
    val = input(f"Enter the element of list # {count},\n"
                f"to exit enter \"q\".\n")
    if val == "q":
        quit_ = True
        continue
    if not is_number(val):
        print("You entered incorrect data")
        continue
    list2.append(float(val))
    count += 1

list3 = [round(x+y, 2)
         for x, y
         in zip_longest(list1, list2, fillvalue=0.)]

print(list1)
print(list2)
print(list3)
