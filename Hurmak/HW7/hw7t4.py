phrase = input('Enter a string: ').split()
resultDict = {}
for i in set(phrase):
    resultDict[i] = phrase.count(i)
print(resultDict)
