import random


matrix = [[random.randint(1,10) for x in range(5)] for y in range(5)]
sum_column = [sum(x[i] for x in matrix) for i in range(len(matrix[0]))]
matrix.append(sum_column)
sum_row = [sum(x) for x in matrix]
for i in range(len(sum_row)):
    matrix[i].append(sum_row[i])
print(f'{matrix}\n{sum_column = }\n{sum_row = }')