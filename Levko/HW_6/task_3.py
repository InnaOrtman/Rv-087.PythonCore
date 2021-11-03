# task_3

import random

M, N = 4, 4
matrix = [[random.randrange(0, 10) for y in range(M)] for x in range(N)]
for im in range(N):
    print(matrix[im])

i = 0
list1 = []
for im in range(M):
    x = ([x[i] for x in matrix])
    list1.append(min(x))
    i += 1
print(f"мінімальні елементи стовпців матриці:\n{list1}")
print(f"максимальний елемент серед мінімальних елементів стовпців матриці:\n{max(list1)}")
