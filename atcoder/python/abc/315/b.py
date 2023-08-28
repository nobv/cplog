# https://atcoder.jp/contests/abc315/tasks/abc315_b
M = int(input())
D = [int(i) for i in input().split()]
total = sum(D)
mid = (total + 1) // 2
month = 0
tmp = 0
for i in range(len(D)):
    if tmp + D[i] >= mid:
        break
    month = i + 1
    tmp += D[i]

day = 0
for j in range(D[month]):
    tmp += 1
    if tmp == mid:
        day = j
        break

print(f"{month + 1} {day + 1}")
