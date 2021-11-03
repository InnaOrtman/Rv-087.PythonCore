matrix = []

for i in range(10):
    matrix.append([])
    for j in range(10):
        matrix[i].append(10*i + j)
        
print(matrix)