#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'flippingMatrix' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY matrix as parameter.
#

def flippingMatrix(matrix):
    # Write your code here
    """
    解いた時に考えたこと


    全然わからなかった
    """
    reversed_rows = []
    for row in matrix:
        _max = max(row)
        if _max == row[0]:
            reversed_rows.append(row)
        else:
            row.reverse()
            reversed_rows.append(row)



if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        print(str(result) + '\n')
        # fptr.write(str(result) + '\n')

    # fptr.close()

