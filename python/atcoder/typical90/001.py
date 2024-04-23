# https://atcoder.jp/contests/typical90/tasks/typical90_a
# https://github.com/E869120/kyopro_educational_90/blob/main/problem/001.jpg

# N, L = map(int, input().split())
# K = int(input())
# A = map(int, input().split())
#

i = int(input())
b = format(i, "b")
f = False
res = []
tmp = ""
for s in b:
    f = s == "1"
    if f and tmp != "":
        res.append(tmp)
        tmp = ""
        continue
    if not f:
        tmp += s
print(res)
print(len(max(res)))
