# task_2
"""
це все звичайно було б доцільніше зробити імпортувавши бібліотеку numpy,
але я вирішила погратися з цим вручну для кращого розуміння матриць(в мене прогалина
з ними ще з універу;)))
"""
import random

print("просто матриця")
M, N = 3, 4
matrix = [[random.randrange(0, 10) for y in range(M)] for x in range(N)]
for im in range(N):
    print(matrix[im])

print("матриця з додатковим рядком (з суми стовпців)")
i = 0
list = []
for im in range(M):
    x = ([x[i] for x in matrix])
    x = sum(x)
    list.append(x)
    i += 1
matrix.append(list)
for im in range(N+1):
    print(matrix[im])

print("матриця з додатковим стовпцем (з суми рядків)")
n = 0
for im in range(N+1):
    y = sum(matrix[n])
    matrix[n].append(y)
    n += 1
for im in range(N+1):
    print(matrix[im])

