N = int(input())
cups = [list(map(int, input().split())) for _ in range(N)]
cups = sorted(cups, reverse=True, key=lambda x: x[1])

total = 0
for fi, si in cups:
    tmp = 0
    for fj, sj in cups:
        if fi != fj:
            tmp = si + sj
        else:
            tmp = si + (sj // 2)

        if total < tmp:
            total = tmp
print(total)
