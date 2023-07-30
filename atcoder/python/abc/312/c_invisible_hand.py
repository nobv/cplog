# https://atcoder.jp/contests/abc312/tasks/abc312_c
# editorial: https://atcoder.jp/contests/abc312/editorial/6859
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(sorted(A + list(map(lambda x: x + 1, B)))[M - 1])
