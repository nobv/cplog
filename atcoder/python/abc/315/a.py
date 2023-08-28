# https://atcoder.jp/contests/abc315/tasks/abc315_a
S = input()
ans = [s for s in S if s not in ("a", "e", "i", "o", "u")]
print("".join(ans))
