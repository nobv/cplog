# https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem
# !/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    """
    解いた時に考えたこと

    単純に配列の中から、正の数、負の数、0 をフィルタリングして計算すればいいと思ったから
    """
    length = len(arr)
    positive = [a for a in arr if a > 0]
    negative = [a for a in arr if a < 0]
    zero = [a for a in arr if a == 0]

    print(len(positive) / length)
    print(len(negative) / length)
    print(len(zero) / length)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
