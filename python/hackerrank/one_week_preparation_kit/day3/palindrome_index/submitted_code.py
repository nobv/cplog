# https://www.hackerrank.com/test/crlnp8rgs12/questions/a2b68fq8p7b
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
    解いた時に考えたこと

    1. 文字列の出現回数を値にしたセットを作る
    2. この時、セットの長さが1の場合はすべて同じ文字列のため -1 を返す
    3. 出現回数が一番少ないものを削除すれば、回文になるはずなので、値が一番小さいもののキーを得る
    4. 次に、文字列のインデックスを値にしたセットを作る
    5. 3 で得たキーの値 (インデックス番号) を返す

    1つだけテストが通ったが、ほかは間違い or タイムアウト
    """
    count_table = {c: s.count(c) for c in s}
    if len(count_table) == 1:
        return -1
    index_table = {c: i for i, c in enumerate(s)}
    remove_key = min(count_table, key=count_table.get)
    return index_table[remove_key]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    q = int(input().strip())

    for q_itr in range(q):
        s = input()

        result = palindromeIndex(s)

        fptr.write(str(result) + "\n")

    fptr.close()
