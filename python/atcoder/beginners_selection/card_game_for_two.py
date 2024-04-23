# https://atcoder.jp/contests/abs/tasks/abc088_b
N = int(input())
a_list = list(map(int, input().split()))
a_list.sort(reverse=True)
alice = []
bob = []
for i, a in enumerate(a_list):
    if i % 2 != 0:
        bob.append(a)
    else:
        alice.append(a)
print(sum(alice) - sum(bob))


# n = int(input())
# a = list(map(int, input().split()))
# a.sort(reverse=True)
#
# ans = 0
# for i in range(len(a)):
#     if i%2==0:
#         ans += a[i]
#     else:
#         ans -= a[i]
#
# print(ans)
