#!/usr/bin/env python3
# generateMatrix

import random


def generateMatrix(rows: int, cols: int, scale: int = 100) -> list:
    """ Generate 2D Matrix  """
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            matrix[i].append(random.randint(0, scale))
    return matrix


def output2DMatrix(matrix):
    """ Output of 2D matrix  """
    j = ""
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(f"{str(matrix[i][j]):^7}", end="")
        print()
    print(("=" * (j + 1) * 7))
