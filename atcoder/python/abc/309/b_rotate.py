# https://atcoder.jp/contests/abc309/tasks/abc309_b
N, *A = open(0).read().split()
N_int = int(N)
res = [["" for _ in range(N_int)] for _ in range(N_int)]


def is_top(i, j):
    return i == 0 and j < len(A) - 1


def is_left(j):
    return j == len(A) - 1


def is_bottom(i):
    return i == len(A) - 1


def is_right(j):
    return j == 0


for i in range(N_int):
    for j in range(N_int):
        if is_top(i, j):
            res[i][j + 1] = A[i][j]
        elif is_right(j):
            res[i - 1][j] = A[i][j]
        elif is_bottom(i):
            res[i][j - 1] = A[i][j]
        elif is_left(j):
            res[i + 1][j] = A[i][j]
        else:
            res[i][j] = A[i][j]
for ans in res:
    print("".join(ans))
