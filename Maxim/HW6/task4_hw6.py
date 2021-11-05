# Task 4
# Divide the tuple into several ones, each of which contains only
# numbers, only letters, etc.

import re


someTuple = ("f", 1, 33, "G", "/", 0.2, "/n",
             "FG", ".", 55, "//", 2, "'", "Gs")
lst1, lst2, lst3 = [], [], []

pat = re.compile(r'\d')
pat2 = re.compile(r'^[a-z]|^[A-z]')
pat3 = re.compile(r'^[a-z]|^[A-z]')

for i in someTuple:
    res = pat.findall(str(i))
    res2 = pat2.findall((str(i)))
    if res:
        lst1.append(i)
    elif res2:
        lst2.append(i)
    else:
        lst3.append(i)

print(tuple(lst1))
print(tuple(lst2))
print(tuple(lst3))
