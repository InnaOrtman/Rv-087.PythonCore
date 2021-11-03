import random


MATRIX_SIZE = 5
matrix = []

for i in range(MATRIX_SIZE):
    matrix.append([])
    for j in range(MATRIX_SIZE):
        matrix[i].append(random.randint(1, 100))

matrix.append([])
for i in range(MATRIX_SIZE):

    matrix[i].append(sum(matrix[i]))
    summary = 0
    for j in range(MATRIX_SIZE):
        summary += matrix[j][i]
    matrix[-1].append(summary)

for i in matrix:
    print(f"row {matrix.index(i)+1} = {i}]")



