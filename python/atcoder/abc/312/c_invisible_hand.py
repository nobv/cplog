# https://atcoder.jp/contests/abc312/tasks/abc312_c
# editorial: https://atcoder.jp/contests/abc312/editorial/6859
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(sorted(A + list(map(lambda x: x + 1, B)))[M - 1])


# other answer
# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# wa = 0
# ac = 1001001001
# while wa + 1 < ac:
#     wj = int((wa + ac) / 2)
#     na = nb = 0
#     for i in range(N):
#         if A[i] <= wj:
#             na += 1
#     for i in range(M):
#         if B[i] >= wj:
#             nb += 1
#     if na >= nb:
#         ac = wj
#     else:
#         wa = wj
# print(ac)
