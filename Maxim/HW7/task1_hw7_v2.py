# Task 1
# Character string is given. Develop a program that removes
# from this line all repeated occurrences of numbers and
# signs of arithmetic operations.

import string


strCharacters = "f23 fds + 34 55- 34 5* 23+ d + 342/ 4321x /"

newStrCharacters = []
patt = set([*string.digits] + ["+", "-", "/", "*", "%"])
uniqueCharacters = set()

print(strCharacters)
strCharacters = list(strCharacters)
while strCharacters:
    item = strCharacters.pop(0)
    if item not in patt:
        newStrCharacters.append(item)
        continue
    if item not in uniqueCharacters:
        uniqueCharacters.add(item)
        newStrCharacters.append(item)

print("".join(newStrCharacters))
