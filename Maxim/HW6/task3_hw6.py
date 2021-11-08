# Task 3
# Find the maximum element among the minimum elements of the matrix columns

from checkInput import checkInputPosNat
from matrix import generateMatrix
from matrix import output2DMatrix


lstValues = [input("Enter the number of rows: "),
             input("Enter the number of cols: ")]

if checkInputPosNat(lstValues):
    lstValues = list(map(int, lstValues))
    matrix = generateMatrix(*lstValues)
    # matrix = generateMatrix(int(lstValues[0]), int(lstValues[1]))

    output2DMatrix(matrix)

    # minimum elements in cols
    lstMinInCols = []
    minNum = int()
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            if j == 0:
                minNum = matrix[j][i]
            elif minNum > matrix[j][i]:
                minNum = matrix[j][i]
        lstMinInCols.append(minNum)

    # print(lstMinInCols)
    for i in range(len(lstMinInCols)):
        print(f"{lstMinInCols[i]:^7}", end="")
    print()

    print(f"Maximum element among the minimum: {max(lstMinInCols)}")
