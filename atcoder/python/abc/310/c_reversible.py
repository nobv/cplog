# https://atcoder.jp/contests/abc310/tasks/abc310_c
N = int(input())
res = set()
for i in range(N):
    S = input()
    res.add(min(S, S[::-1]))
print(len(res))
