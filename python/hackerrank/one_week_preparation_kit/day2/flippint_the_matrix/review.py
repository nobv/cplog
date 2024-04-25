# https://www.hackerrank.com/challenges/flipping-the-matrix/problem
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
    解説
    https://zenn.dev/aozou/articles/93e6343d825ab0
    https://www.youtube.com/watch?v=4rin1enhuQQ&t=62s

    これが一番分かりやすかった
    https://www.youtube.com/watch?v=KNj0L_Rqp7Q


    """
    _n = len(matrix)
    n = _n - 1
    middle = _n // 2
    result = 0
    for i in range(middle):
        for j in range(middle):
            current_matrix = []
            current_matrix.append(matrix[i][j])  # left_top
            current_matrix.append(matrix[n - 1][j])  # left_bottom
            current_matrix.append(matrix[i][n - j])  # right_top
            current_matrix.append(matrix[i - 1][j - 1])  # right_bottom
            result += max(current_matrix)
    return result


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        matrix = []

        for _ in range(2 * n):
            matrix.append(list(map(int, input().rstrip().split())))

        result = flippingMatrix(matrix)

        print(str(result) + "\n")
        fptr.write(str(result) + "\n")

    fptr.close()
