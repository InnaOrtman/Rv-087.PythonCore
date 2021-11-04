import random


list1 = []
matrixSize = random.randint(3, 10)
for i in range(0, matrixSize):
    list1.append([])
    for j in range(0, matrixSize):
        list1[i].append(random.randint(1, 101))
    print(list1[i])

print('='*10)
sumRow = []

for i in range(0, matrixSize):
    list1[i].append(sum(list1[i]))
    print(list1[i])
for i in range(0, matrixSize+1):
    sumCol = 0
    for j in range(0, matrixSize):
        sumCol += list1[j][i]
    sumRow.append(sumCol)
print(sumRow)
list1.append(sumRow)
print('='*10)
