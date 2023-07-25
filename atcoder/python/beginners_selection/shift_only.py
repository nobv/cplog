# https://atcoder.jp/contests/abs/tasks/abc081_b
n = int(input())
a_list_len = [_n for _n in range(n)]
a_list = list(map(int, input().split(" ")))

count = 0
while True:
    if all([True if a % 2 == 0 else False for a in a_list]):
        a_list = [int(a / 2) for a in a_list]
        count += 1
    else:
        break
print(count)
