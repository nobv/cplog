# https://www.hackerrank.com/challenges/one-week-preparation-kit-grid-challenge/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gridChallenge' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING_ARRAY grid as parameter.
#


def gridChallenge(grid):
    # Write your code here
    """
    解いた時に考えたこと

    1. 行をソートする
    2. 行と列を入れ替える
    3. 行 (行と列を入れ替えたので、元々は列だったもの) がアルファベット順かどうかを確認 (次の文字列と比較して確認)
    """
    # sort rows
    sorted_grid = [sorted(row) for row in grid]

    # swap row and column
    swapped_grid = [list(x) for x in zip(*sorted_grid)]

    for row in swapped_grid:
        for i in range(len(row) - 1):
            if row[i] > row[i + 1]:
                return "NO"
    return "YES"


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        grid = []

        for _ in range(n):
            grid_item = input()
            grid.append(grid_item)

        result = gridChallenge(grid)

        fptr.write(result + "\n")

    fptr.close()
