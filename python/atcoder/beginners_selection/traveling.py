# https://atcoder.jp/contests/abs/tasks/arc089_a
n = int(input())
for i in range(n):
    t, x, y = map(int, input().split())
    dist = x + y
    if t < dist or (dist % 2) != (t % 2):
        print("No")
        exit()
print("Yes")
