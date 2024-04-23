N, M = map(int, input().split())
if M == 1:
    print(1)
    exit()
A = sorted(
    [list(map(int, input().split())) for _ in range(N)],
    reverse=True,
    key=lambda x: x[2],
)
print(A)
total = 0
previous = []
routes = []
for ai in A:
    town_a_i, town_b_i, length_i = ai
    previous.append(ai)
    for aj in [filtered_A for filtered_A in A if filtered_A not in previous]:
        town_a_j, town_b_j, length_j = aj
        d = list(set([town_a_i, town_b_i]) & set([town_a_j, town_b_j]))
        if len(d) == 0:
            break
        _to = d[0]
        _from = town_b_i if town_a_i == _to else town_a_i
        if _from in routes or _to in routes:
            break
        routes.append(_from)
        total += length_i
print(total)
