# task_4

text = input("Enter the sentence, please:\n").lower()
x = text.split()

y = dict()
for i in x:
    y[i] = x.count(i)

print(y)
