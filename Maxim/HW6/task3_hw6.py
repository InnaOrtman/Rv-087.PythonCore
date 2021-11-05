# Task 3
# Find the maximum element among the minimum elements of the matrix columns

from checkInput import checkInputPosNat
from matrix import generateMatrix
from matrix import output2DMatrix


lstValues = [input("Enter the number of rows: "),
             input("Enter the number of cols: ")]

if checkInputPosNat(lstValues):
    matrix = generateMatrix(int(lstValues[0]), int(lstValues[1]))  # to ask Kate

    output2DMatrix(matrix)
    print("=" * int(lstValues[1])*5)

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
    print(lstMinInCols)
    print(f"Maximum element among the minimum: {max(lstMinInCols)}")
