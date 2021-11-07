import random


matrix = []
minlist = []
matrixSize = random.randint(3, 10)
for i in range(0, matrixSize):
    matrix.append([])
    for j in range(0, matrixSize):
        matrix[i].append(random.randint(1, 101))
    print(matrix[i])
print('='*30)
while matrix[0]:
    colList = []
    for i in matrix:
        colList.append(i[-1])
        i.pop()
    minlist.append(min(colList))
print(minlist[::-1])
print('='*30)
print(max(minlist))
