numTuple = (1, 2, 3, 4, 5, 6, 7, 8, 9)
for i in numTuple:
    print(f'{"-" * 10}')
    for j in numTuple:
        print(f'{i} * {j} = {i*j}')
