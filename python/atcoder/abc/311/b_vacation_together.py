# https://atcoder.jp/contests/abc311/tasks/abc311_b
N, D = map(int, input().split())
S = [input() for _ in range(N)]
ans = cur = 0
for j in range(D):
    can = 1
    for i in range(N):
        can &= S[i][j] == "o"
    cur = cur + 1 if can else 0
    ans = max(ans, cur)
print(ans)
