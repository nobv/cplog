# https://atcoder.jp/contests/abc309/tasks/abc309_a
A, B = map(int, input().split())
board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
for b in board:
    if set([A, B]).issubset(b):
        print("Yes")
        exit()
print("No")
