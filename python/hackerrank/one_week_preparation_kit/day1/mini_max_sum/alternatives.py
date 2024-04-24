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
    問題文:
        5 つの正の整数が与えられた場合、5 つの整数のうち 4 つを正確に合計することによって計算できる最小値と最大値を見つけます。次に、それぞれの最小値と最大値を、スペースで区切られた 2 つの長整数の 1 行として出力します。

    この解法の考え方:
        `5 つの整数のうち 4 つを正確に合計することによって計算できる最小値と最大値を見つけます` というところがポイント

        まずは合計を出す
        ```py
        arr = [1, 2, 3, 4, 5]
        _sum = sum(arr)
        # 15
        ```

        合計から、配列の最大値(5)を引くと最小値が得られる (15 - 5 = 10)
        逆に、合計から配列の最小値(1)を引くと最大値が得られる (15 - 1 = 14)

        その他の計算結果は以下の通り
        1. Sum everything except 1. the sum is 2 + 3 + 4 + 5 = 14.
        2. Sum everything except 2. the sum is 1 + 3 + 4 + 5 = 13.
        3. Sum everything except 3. the sum is 1 + 2 + 4 + 5 = 12.
        4. Sum everything except 4. the sum is 1 + 2 + 3 + 5 = 11.
        5. Sum everything except 5. the sum is 1 + 2 + 3 + 4 = 10.

    """
    _sum = sum(arr)
    print(_sum)
    _max = _sum - min(arr)
    _min = _sum - max(arr)
    print(f"{_max} {_min}")


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
