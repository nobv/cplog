# https://www.hackerrank.com/challenges/one-week-preparation-kit-caesar-cipher-1/problem
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#


def caesarCipher(s, k):
    # Write your code here
    """
    解説

    - https://www.youtube.com/watch?v=UkYubOj2ttA
    - https://qiita.com/TodayInsane/items/94f495db5ba143a8d3e0

    chr で Unicodeコードポイントから文字列を返し、ord で文字列から Unicode コードポイントを返すというところがポイント
    - https://docs.python.org/ja/3.11/library/functions.html#chr
    - https://docs.python.org/ja/3.11/library/functions.html#ord

    さらに、Z, z から A, a に戻ることも考慮する必要がある
    コードポイントは大文字と小文字で区別されているため、それぞれの場合で計算する必要がある
    例: c == "z", k == 2 の場合
    1. ord(c) から ord('a') + k を引いた値を算出 => 27
    2. 更にその値を 26 (アルファベットの文字数)で割ったあまりを計算 => 1
    3. その値に ord("a") を足す => 98 == "b"

    """
    res = ""
    for c in s:
        if c.islower():
            res += chr((ord(c) - ord("a") + k) % 26 + ord("a"))
        elif c.isupper():
            res += chr((ord(c) - ord("A") + k) % 26 + ord("A"))
        else:
            res += c
    return res


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + "\n")

    fptr.close()
