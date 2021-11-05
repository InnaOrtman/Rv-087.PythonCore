#!/usr/bin/env python3
# generateMatrix

import random


def generateMatrix(rows: int, cols: int) -> list:
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            matrix[i].append(random.randint(0, 100))
    return matrix


def output2DMatrix(matrix):
    """ Output of 2D matrix  """
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            lenElement = len(str(matrix[i][j]))
            if lenElement == 1:
                print(matrix[i][j], end="    ")
            elif lenElement == 2:
                print(matrix[i][j], end="   ")
            else:
                print(matrix[i][j], end="  ")
        print()
