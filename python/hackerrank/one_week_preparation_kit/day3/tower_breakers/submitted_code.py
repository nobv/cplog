# https://www.hackerrank.com/challenges/one-week-preparation-kit-tower-breakers-1/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'towerBreakers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#


def towerBreakers(n, m):
    # Write your code here
    """
    解説

    - https://www.youtube.com/watch?v=jOxTTE3IkjE
    - https://coderforyou.medium.com/tower-breakers-hackerrank-solution-3dcc75e6a881

    - ルールを理解することが重要
      - 各プレイヤーは、ターン中に1つのタワーのみしか変更することが出来ない
      - タワーのサイズを 0 にすることが出来ない (1 <= y < x という制約)
      - プレイヤーのターン中、タワーのサイズがどれだけあっても1つにすることが出来る (1 <= y < x という制約)
      - 上記の制約により、以下のことがわかる
        - タワーのサイズが1つの場合は必ずプレイヤー2が勝利する (このゲームは必ずプレイヤー1のターンから始まるかつ、タワーのサイズを0にすることが出来ないためプレイヤー1は何も出来ない)
        - タワーが1つの場合は必ずプレイヤー1が勝利する (このゲームは必ずプレイヤー1のターンから始まるかつ、タワーのサイズを1にすることが出来る。次のターン、プレイヤー2は何も出来ない)
        - タワーの数が偶数の場合は、必ずプレイヤー2が勝利する
        - タワーの数が奇数の場合は、必ずプレイヤー1が勝利する

    """
    if m == 1 or n % 2 == 0:
        return 2
    else:
        return 1


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        result = towerBreakers(n, m)

        fptr.write(str(result) + "\n")

    fptr.close()
