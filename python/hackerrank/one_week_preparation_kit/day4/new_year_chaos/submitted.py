# https://www.hackerrank.com/challenges/one-week-preparation-kit-new-year-chaos/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#


def minimumBribes(q):
    # Write your code here
    """
    解いた時に考えたこと

    q と、q をソートした数列同士の i 番目比較を比較
    その差が `2以下` であれば、賄賂を渡して順番を入れ替えたとする

    ただ、このコードだとすべてのテストが通らなかった
    """
    sorted_q = sorted(q)
    bribes = 0
    is_chaotic = False
    for i in range(len(q) - 2):
        if q[i] == sorted_q[i]:
            continue
        elif q[i] != sorted_q[i] and abs(q[i] - sorted_q[i]) <= 2:
            # q[i] と sorted_q[i] が異なり、かつ q[i] - sorted_q[i] の絶対値が 2以下であれば賄賂を贈ったとする
            bribes += 1
        else:
            is_chaotic = True
            break
    print(bribes) if not is_chaotic else print("Too chaotic")


if __name__ == "__main__":
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
