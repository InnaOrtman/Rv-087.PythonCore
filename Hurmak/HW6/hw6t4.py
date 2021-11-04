tup = 1, '34', 2, 'wqfe', '*'
numTuple = []
alphaTuple = []
otherTuple = []
for i in tup:
    if str(i).isnumeric():
        numTuple.append(i)
    elif str(i).isalpha():
        alphaTuple.append(i)
    else:
        otherTuple.append(i)
print(tuple(numTuple))
print(tuple(alphaTuple))
print(tuple(otherTuple))
