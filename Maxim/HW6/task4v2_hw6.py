# Task 4
# Divide the tuple into several ones, each of which contains only
# numbers, only letters, etc.

from mynum import is_number
from mynum import if_number_to_float
from mynum import if_int_to_int


someTuple = ("f", 1, 33, "G", "/", 0.2, "/n",
             "FG", ".", 55, "//", 2, "'", "Gs")
lst1, lst2, lst3 = [], [], []

for i in range(len(someTuple)):
    val = str(someTuple[i])
    if is_number(val):
        val = if_int_to_int(
            if_number_to_float(val))
        lst1.append(val)
    elif val.isalpha():
        lst2.append(val)
    else:
        lst3.append(val)

print(tuple(lst1))
print(tuple(lst2))
print(tuple(lst3))
