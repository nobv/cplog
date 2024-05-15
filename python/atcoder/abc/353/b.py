# https://atcoder.jp/contests/abc353/tasks/abc353_b
N, K = map(int, input().split())
A = [int(i) for i in input().split(" ")]

group_list = A

started = 1
current_group = 0
for group in group_list:
    if (current_group + group) <= K:
        current_group += group
    else:
        started += 1
        current_group = 0
        current_group += group

print(started)
