userText = """Task 4
User enters the text. A word is a sequence of non-empty characters
that follow in a row, words are separated by one or more spaces.
Create a dictionary in which the keys are the words from the sentence,
and the values - the number of it's occurrences in the sentence."""

setUserText = set()
dictWords = dict()

userTextClear = []
toDel = (",", ".", ":", "-")
for i in userText:
    if i in toDel:
        continue
    userTextClear.append(i)
userTextClear = "".join(userTextClear).split()

while userTextClear:
    word = userTextClear.pop()
    if word not in setUserText:
        setUserText.add(word)
        dictWords[word] = 1
    else:
        dictWords[word] += 1

for k, v in dictWords.items():
    print(k, ": ", v)
