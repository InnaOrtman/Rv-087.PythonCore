# Task 4
# Divide the tuple into several ones, each of which contains only
# numbers, only letters, etc.

import re


someTuple = ("f", 1, 33, "G", "/", 0.2, "/n", 1.,
             "FG", ".", 55, "//", 2, "'", "Gs", "s5", "2s")
lst1, lst2, lst3 = [], [], []

pat1 = re.compile(r'^\d+\.?\d+$|^\d+$')
pat2 = re.compile(r'^[A-z]+$')

for i in someTuple:
    res1 = pat1.findall(str(i))
    res2 = pat2.findall(str(i))
    if res1:
        lst1.append(i)
    elif res2:
        lst2.append(i)
    else:
        lst3.append(i)

print(tuple(lst1))
print(tuple(lst2))
print(tuple(lst3))
