# https://atcoder.jp/contests/abc310/tasks/abc310_a
N, P, Q = map(int, input().split())
D = list(map(int, input().split()))
_min = min(list(map(lambda x: x + Q, D)))
print(_min if _min < P else P)
