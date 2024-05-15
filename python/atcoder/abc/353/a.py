# https://atcoder.jp/contests/abc353/tasks/abc353_a
N = int(input())
H = [int(i) for i in input().split(" ")]
target = H[0]
result = -1
for i, v in enumerate(H):
    if target < v:
        result = i
        break
if result != -1:
    print(result + 1)
else:
    print(result)
