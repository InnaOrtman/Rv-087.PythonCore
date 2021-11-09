# task_4

wordList = "My name is Inna Inna"
x = wordList.split()

y = dict()
for i in x:
    y[i] = x.count(i)

print(y)
