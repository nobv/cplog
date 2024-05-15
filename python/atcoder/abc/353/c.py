# https://atcoder.jp/contests/abc353/tasks/abc353_c

# 以下 TLE になったコード
# N = int(input())
# A = [int(i) for i in input().split(" ")]

# total = 0
# for i in range(N - 1):
#     for j in range(i + 1, N):
#         total += (A[i] + A[j]) % pow(10, 8)
# print(total)


# 解説
# https://www.youtube.com/watch?v=Cw29uys1JV0&t=2038s
# https://atcoder.jp/contests/abc353/editorial/9957
# https://atcoder.jp/contests/abc353/editorial/9975
# https://note.com/igasu_7/n/n60b400d091e6
# (x + y) % (10 ** 8) がどういう挙動をするかを考える
# x, y が小さい場合で考える。また、10**8ではなく、10で考える
# 例えば、
#   1. x + y = 2 だとすると、2 % 10 = 2
#   2. x + y = 75 だとすると、75 % 10 = 5
# つまり、
#   1. のように、x + y が 10 より小さい場合は x + y
#   2. のように、x + y が 10 より大きい場合は x + y - 7(商) * 10
# と考える事ができる
# つまり、
#   x + y < 10 ** 8  だと引き算をする必要はない
#   x + y >= 10 ** 8 だと引き算をする必要がある
# このことから、仮に x + y が 10 ** 8 以上になる回数が分かれば、`その回数 * 10 ** 8` を引けばいいことがわかる

# 尺取法 (公式解説)
N = int(input())
A = [int(i) for i in input().split(" ")]

M = 10**8
A.sort()
r = N
cnt, res = 0, 0
for i in range(N):
    r = max(r, i + 1)
    while r - 1 > i and A[r - 1] + A[i] >= M:
        r -= 1
    cnt += N - r
for i in range(N):
    res += A[i] * (N - 1)
res -= cnt * M
print(res)


# 2分探索 (公式解説動画 ver)
N = int(input())
A = [int(i) for i in input().split(" ")]

M = 10**8
A.sort()
ans = 0

# (x + y) が 10 ** 8 未満である
for i in range(N):
    #
    ans += A[i] * (N - 1)

r = N - 1
for i in range(N):
    while r > 0 and A[r] + A[i] >= M:
        r -= 1
    ans -= (N - max(r, i) - 1) * M
print(ans)

# 2分探索 (めぐる式 ver)
# https://qiita.com/mattsunkun/items/7a715be2a9fcc244b533#c%E5%95%8F%E9%A1%8C
# これが一番分かりやすかった
N = int(input())
A = [int(i) for i in input().split(" ")]
A.sort()
M = 10**8

# 和が MOD を超えた回数
cnt = 0
for i in range(N - 1):
    ng = i  # 現在注目しているAの位置
    ok = N  # 右端
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        if A[mid] + A[i] >= M:
            ok = mid
        else:
            ng = mid
    cnt += N - ok
# A総和の(N-1)倍から、10**8を超えた回数に10**8の積を引く
# なぜ N-1 かというと、 x + y の組み合わせを考えた時に、自信は含めないため
print(sum(A) * (N - 1) - (cnt * M))
