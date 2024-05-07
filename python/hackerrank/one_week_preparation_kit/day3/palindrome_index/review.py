#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#


def palindromeIndex(s):
    # Write your code here
    """
    問題: https://www.hackerrank.com/challenges/palindrome-index/problem

    解説
    - https://www.youtube.com/watch?v=YSGWqoIBuOM
    - https://www.youtube.com/watch?v=gd4hCrbYAMg
    - https://www.youtube.com/watch?v=RVm_0iQdwzw
      - これが一番良さそうな解法だった
    """
    n = len(s)
    reversed_s = s[::-1]  # 文字列を逆順にする

    if s == reversed_s:  # s と反転した文字列が同じ場合は回文
        return -1

    for i in range(n):
        # s から i 番目の文字を削除した文字列を作る (i番目より前の部分 s[:i] と i番目より後ろの部分 s[i + 1:] を取り出し連結することにより、i番目の文字を削除した文字列が出来る)
        # s = "abcde", i = 2 の場合、 s[:i] = "ab" s[i + 1:] = "de" 結合すると "abde" になる
        new_s = s[:i] + s[i + 1 :]
        # reserved_s から、new_s と同様に i番目の文字列を削除した文字列を作っている
        # ただし、reserved_s は逆順の文字のため削除する位置が異なるため n - i - 1 としている
        # reserved_s = "edcba", n = 5, i = 2 の場合、 reserved_s[:n-i-1] = "ed" reserved_s[n-i:] = "a"
        new_reversed_s = reversed_s[: n - i - 1] + reversed_s[n - i :]

        if new_s == new_reversed_s:
            return i

    return -1


if __name__ == "__main__":
    # fptr = open(os.environ["OUTPUT_PATH"], "w")

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        # fptr.write(str(result) + "\n")
        print(str(result) + "\n")

    # fptr.close()
