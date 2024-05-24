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
    解説
        - https://csanim.com/tutorials/hackerrank-solution-new-year-chaos
        - https://medium.com/@dwang0816/new-year-chaos-41e8e56cb342
        - https://www.youtube.com/watch?v=LgszjFykAbE
            面白い解き方だった

    """

    # https://csanim.com/tutorials/hackerrank-solution-new-year-chaos ver.
    bribes = 0

    for i, o in enumerate(q):
        cur = i + 1

        if o - cur > 2:
            print("Too chaotic")
            return

        for k in q[max(o - 2, 0) : i]:
            if k > o:
                bribes += 1

    print(bribes)

    # https://www.youtube.com/watch?v=LgszjFykAbE ver.
    bribes = 0
    p1 = 1
    p2 = 2
    p3 = 3
    for i in range(len(q)):
        if q[i] == p1:
            p1 = p2
            p2 = p3
            p3 += 1
        elif q[i] == p2:
            bribes += 1
            p2 = p3
            p3 += 1
        elif q[i] == p3:
            bribes += 2
            p3 += 1
        else:
            print("Too chaotic")
            return
    print(bribes)


if __name__ == "__main__":
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
