# Task 5
# Enter a number, letter or special character from the keyboard and
# return the entry index to the corresponding tuple accordingly.

import string


lstSpec = (list(string.punctuation)
           + [r"\n", r"\b", r"\f", r"\r", r"\t", r"\v", r"\a",
              r"\N", r"\u", r"\U", r"\x", r"\o", r"\0"])
someTuple = (
    tuple(string.digits),
    tuple(string.ascii_letters),
    tuple(lstSpec)
)

userInput = input(r"Enter a number, letter or special character: ")
found = False
print(someTuple)

for i in range(len(someTuple)):
    if userInput in someTuple[i]:
        print(f"Entry index: [{i}][{someTuple[i].index(userInput)}]")
        found = True
        break
if not found:
    print(f"The element {userInput} not found")
