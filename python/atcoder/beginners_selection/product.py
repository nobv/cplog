# https://atcoder.jp/contests/abs/tasks/abc086_a
a, b = map(int, input().split(" "))
product = a * b
if (product % 2) == 0:
    print("Even")
else:
    print("Odd")
