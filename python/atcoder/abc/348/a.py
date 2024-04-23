# https://atcoder.jp/contests/abc348/tasks/abc348_a
N = int(input())
results = []
for i in range(1, N + 1):
    if i % 3 == 0:
        results.append("x")
    else:
        results.append("o")
print("".join(results))
