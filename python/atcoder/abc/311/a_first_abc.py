# https://atcoder.jp/contests/abc311/tasks/abc311_a
N = int(input())
S = input()
a = b = c = False
for i in range(N + 1):
    if a and b and c:
        print(i)
        exit()
    if S[i] == "A":
        a = True
    if S[i] == "B":
        b = True
    if S[i] == "C":
        c = True
