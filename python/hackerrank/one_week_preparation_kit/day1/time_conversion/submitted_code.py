# https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion/problem
#!/bin/python3

import math
import os
import random
import re
import sys
from datetime import datetime


#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    """
    解いた時に考えたこと

    PM かつ 時間が 12 未満の場合は +12 をする
    AM かつ 時間が 12 以上の場合は -12 をする

    07:05:45PM で考えると、
    PM かつ、時間が 12 未満なので、+12 をすると 19 になる

    12:40:22AM で考えると、
    AM かつ、時間が 12 以上なので -12 をすると 0 になる

    ここで更に考えたのが、1桁の数値をどう 0埋めするか、ということ
    f文字列で 0埋めを行った `f"{8:02}"` => `08`
    """
    hh = s[0:2]
    mm = s[3:5]
    ss = s[6:8]
    ampm = s[8:10]
    if ampm == "PM" and int(hh) < 12:
        return f"{12 + int(hh):02}:{mm}:{ss}"
    if ampm == "AM" and int(hh) >= 12:
        return f"{int(hh) - 12:02}:{mm}:{ss}"
    return f"{hh}:{mm}:{ss}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
