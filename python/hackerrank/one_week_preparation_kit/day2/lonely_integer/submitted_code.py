# https://www.hackerrank.com/challenges/one-week-preparation-kit-lonely-integer/problem
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    """
    解いた時に考えたこと

    配列の中から、現在の値と同じものを抽出し、なければユニークとみなす
    """
    for current in a:
        result = [target for target in a if target == current]
        if len(result) != 1:
            continue
        else:
            return current


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a)

    fptr.write(str(result) + '\n')

    fptr.close()
