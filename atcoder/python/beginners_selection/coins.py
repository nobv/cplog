# https://atcoder.jp/contests/abs/tasks/abc087_b
a = int(input())
b = int(input())
c = int(input())
x = int(input())

res = 0
for _a in range(a + 1):
    for _b in range(b + 1):
        for _c in range(c + 1):
            total = 500 * _a + 100 * _b + 50 * _c
            if total == x:
                res += 1
print(res)
