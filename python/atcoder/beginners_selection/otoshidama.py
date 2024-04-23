# https://atcoder.jp/contests/abs/tasks/abc085_c
n, y = map(int, input().split())
y = int(y / 1000)
for a in range(n + 1):
    for b in range(n + 1):
        c = n - (a + b)
        if c < 0:
            break
        if 10 * a + 5 * b + c == y:
            print(f"{a} {b} {c}")
            exit()
print("-1 -1 -1")
