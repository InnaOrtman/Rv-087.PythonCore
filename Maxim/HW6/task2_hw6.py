# Task 2
# 	Calculate the sums of each row and each column of the matrix.
# 	Complete it with a column that contains the sums of the elements
# 	of the rows and a row whose elements are the sums of the elements
# 	of the columns.

from checkInput import checkInputPosNat
from matrix import generateMatrix
from matrix import output2DMatrix


lstValues = [input("Enter the number of rows: "),
             input("Enter the number of cols: ")]

if checkInputPosNat(lstValues):
    matrix = generateMatrix(*[int(i) for i in lstValues])
    # [*arr] = map(int, lstValues)
    # matrix = generateMatrix(*arr)
    # matrix = generateMatrix(int(lstValues[0]), int(lstValues[1]))

# Output of matrix without changes
    output2DMatrix(matrix)

# Changes matrix in cols
    matrixChanged = []
    countInCols = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            countInCols += matrix[i][j]
        matrixChanged.append(matrix[i])
        matrixChanged[i].append(countInCols)
        countInCols = 0

# count sum of values in cols and create tempList
    countInRows = 0
    tempList = []
    for i in range(len(matrix[0]) - 1):
        for j in range(len(matrix)):
            countInRows += matrix[j][i]
        tempList.append(countInRows)
        countInRows = 0

# Add tempList to matrixChanged
    matrixChanged.append(tempList)

# Output of changed matrix
    output2DMatrix(matrixChanged)
