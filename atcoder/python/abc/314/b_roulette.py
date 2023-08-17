# https://atcoder.jp/contests/abc314/tasks/abc314_b

N = int(input())
C = []
A = []
for i in range(N):
    C.append(int(input()))
    A.append(list(map(int, input().split())))
X = int(input())

tmp = {}
for i, a in enumerate(A):
    if X in a:
        tmp[i + 1] = C[i]
if len(tmp) == 0:
    print(0)
    exit()

tmp2 = sorted(tmp.items(), key=lambda x: x[1])
t = tmp2[0][1]
res = []
for k, v in tmp2:
    if v <= t:
        res.append(k)
print(len(res))
print(" ".join(map(str, res)))
