# https://atcoder.jp/contests/abs/tasks/abc083_b
n, a, b = list(map(int, input().split(" ")))

total = 0
for i in range(1, n + 1):
    _sum = sum([int(j) for j in str(i)])
    if a <= _sum and b >= _sum:
        total += i
print(total)
