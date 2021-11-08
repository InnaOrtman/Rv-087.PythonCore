stringToCheck = list(input('Enter a string: '))
stringChecked = ''
while len(stringToCheck) >= 1:
    lastSymbol = stringToCheck.pop()
    if not str(lastSymbol).isalpha() and lastSymbol == stringToCheck[-1]:
        continue
    stringChecked += str(lastSymbol)
stringToCheck = stringChecked[::-1]
print(stringToCheck)
