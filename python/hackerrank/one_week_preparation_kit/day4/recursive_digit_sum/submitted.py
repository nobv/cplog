# https://www.hackerrank.com/challenges/one-week-preparation-kit-recursive-digit-sum/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#


def superDigit(n, k):
    # Write your code here

    # 以下タイムアウトになったコード
    # p = n * k
    # total = str(sum(int(i) for i in p))
    # while len(total) > 1:
    #     total = str(sum(int(i) for i in total))
    # return int(total)

    # 数が大きすぎた場合にタイムアウトになってしまうため、 `(k % 9)` をすることが重要
    # これは、任意の整数について、その各桁の数字の和を取ると、元の数とその和は9で割った余りが同じになるという特性を利用している
    #
    p = n * (k % 9)
    total = str(sum(int(i) for i in p))
    while len(total) > 1:
        total = str(sum(int(i) for i in total))
    return int(total)


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)
    print(result)

    # fptr.write(str(result) + "\n")

    # fptr.close()
