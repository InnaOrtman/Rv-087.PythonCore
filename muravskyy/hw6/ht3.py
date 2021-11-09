import random


matrix = [[random.randint(1,100) for x in range(5)] for y in range(5)]
max_in_min = max([min(x) for x in tuple(zip(*matrix))])
print(f'{matrix}\nmax in minimum is {max_in_min}')