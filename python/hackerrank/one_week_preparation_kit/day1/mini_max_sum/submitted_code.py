# https://www.hackerrank.com/challenges/one-week-preparation-kit-mini-max-sum/problem
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    """
    解いた時に考えたこと

    配列をループして、現在走査しているもの以外の合計を保存しておく
    ソートする
    ソートした結果、配列の最初と最後が min と max なはずなのでそれを出力する
    """
    total = []
    for i in range(0, len(arr)):
        total.append(sum([a for j, a in enumerate(arr) if j != i]))
    total.sort()
    print(f"{total[0]} {total[-1]}")


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
