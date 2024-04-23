# https://atcoder.jp/contests/abc310/tasks/abc310_b
N, M = map(int, input().split())
row = []
for _ in range(N):
    row.append(list(map(int, input().split())))

for i in range(N):
    pi, ci, *fi = row[i]
    for j in range(N):
        pj, cj, *fj = row[j]
        if pi >= pj and set(fj).issuperset(fi) and (pi > pj or len(fj) > len(fi)):
            print("Yes")
            exit()
print("No")
