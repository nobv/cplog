# https://atcoder.jp/contests/abs/tasks/arc065_a
s = str(input())[::-1]
reversed_list = [s[::-1] for s in ["dream", "dreamer", "erase", "eraser"]]
cnt = 0
for i in range(len(s)):
    if i == cnt:
        for j in reversed_list:
            if s[i : i + len(j)] == j:
                cnt += len(j)
print("YES" if cnt == len(s) else "NO")
