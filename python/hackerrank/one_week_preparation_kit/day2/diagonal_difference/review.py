# https://www.hackerrank.com/challenges/one-week-preparation-kit-diagonal-difference/problem
#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here

    """
    解いた時に考えたこと


    これは正直わからなかった。
    aとbという2つの変数を初期化します。これらの変数は、それぞれ対角要素と反対側の対角要素の和を格納します。
    forループを使用して、2次元配列arrの各行（サブリスト）を順に処理します。ループ変数iaは、現在処理している行のインデックスを表します。
    各行に対して、対角要素arr[ia][ia]をaに加え、反対側の対角要素arr[ia][-ia - 1]をbに加えます。
    ここで、arr[ia][ia]はia行ia列の要素を、arr[ia][-ia - 1]はia行の末尾からia + 1番目の要素を表します。
    したがって、このコードは2次元配列の対角要素と反対側の対角要素の和を計算します。

    実際にこのコードを実行すると、以下の結果が得られます：

    The sum of the elements at the diagonal positions is 4.
    The sum of the elements at the opposite diagonal positions is 19.

    これは、対角要素（11, 5, -12）の和が4で、反対側の対角要素（4, 5, 10）の和が19であることを示しています。
    arr[ia][-ia - 1]の部分は、2次元配列arrの「反対側の対角線」上の要素を指しています。ここで、「反対側の対角線」とは、右上から左下へと向かう対角線のことを指します。

    まず、arr[ia]はarrのia番目のサブリスト（行）を返します。そして、[-ia - 1]はそのサブリストの末尾からia + 1番目の要素を返します。

    Pythonでは、リストのインデックスは0から始まりますが、負のインデックスを使用するとリストの末尾から要素を取得できます。つまり、-1は最後の要素、-2は最後から2番目の要素、というようになります。

    したがって、arr[ia][-ia - 1]はia行の末尾からia + 1番目の要素を返します。これにより、右上から左下へと向かう「反対側の対角線」上の要素を取得できます。

    例えば、arr = [[11,2,4],[4,5,6],[10,8,-12]]という2次元配列があるとき、arr[0][-0 - 1]（つまりarr[0][-1]）は最初の行の最後の要素4を、arr[1][-1 - 1]（つまりarr[1][-2]）は2行目の最後から2番目の要素5を、arr[2][-2 - 1]（つまりarr[2][-3]）は3行目の最後から3番目（つまり最初）の要素10を返します。
    """
    a, b = 0, 0
    for ia in range(len(arr)):
        a += arr[ia][ia]
        b += arr[ia][-ia - 1]
    return abs(a - b)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
