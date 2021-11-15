stringForEditing = 'EEeee1111::::zzzzzz1999994mmmmmm;;;Arrrrrrtem20000044444'

textToList = list(stringForEditing)
newList = []

for i in range(len(textToList)):
    if textToList[i] != textToList[i-1]:
        newList.append(textToList[i])

    
print('String before: ' ,stringForEditing)
print('String after: ',''.join(newList))