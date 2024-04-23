# https://atcoder.jp/contests/abc309/tasks/abc309_c
def is_ok(mid, key, a, b):
    result = 0
    for i in range(len(a)):
        if mid <= a[i]:
            result += b[i]
    return result <= key


N, K = map(int, input().split())
A = [0] * N
B = [0] * N
for i in range(N):
    A[i], B[i] = map(int, input().split())


ng = 0
ok = 10**9 + 1
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if is_ok(mid, K, A, B):
        ok = mid
    else:
        ng = mid
print(ok)


# wrong anser
# N, K = map(int, input().split())
# a_list = []
# for _ in range(N):
#     a, b = map(int, input().split())
#     a_list.append([a] * b)
# ans = 0
# while True:
#     total = 0
#     for i in a_list:
#         if len(i) > 0:
#             total += i.pop(0)
#     if total <= K:
#         ans += 1
#     else:
#         print(ans)
#         exit()
