N, M, P = map(int, input().split())
if N < M:
    print(0)
    exit()
day = M
ans = 0
while day < N:
    current = day + P
    if current > N:
        break
    day = current
    ans += 1
print(ans + 1)
