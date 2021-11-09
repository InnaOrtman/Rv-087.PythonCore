import random


MATRIX_SIZE = 5
matrix = []
minimums = []

for i in range(MATRIX_SIZE):
    matrix.append([])
    for j in range(MATRIX_SIZE):
        matrix[i].append(random.randint(1, 100))

for i in range(len(matrix)):
    minimum = int(matrix[i][0])

    for j in range(len(matrix)):
        if minimum > matrix[j][i]:
            minimum = matrix[j][i]
    minimums.append(minimum)

for i in matrix:
    print(i)
print(minimums)
print(max(minimums))

