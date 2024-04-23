# https://atcoder.jp/contests/abc348/tasks/abc348_b
N = int(input())
coordinate_list = [list(map(int, input().split(" "))) for _ in range(N)]

for i in range(0, N):
    max_dist = 0
    idx = -1
    x, y = coordinate_list[i]

    for j in range(0, N):
        _x, _y = coordinate_list[j]
        dist = (x - _x) * (x - _x) + (y - _y) * (y - _y)
        if max_dist < dist:
            max_dist = dist
            idx = j
    print(idx + 1)
