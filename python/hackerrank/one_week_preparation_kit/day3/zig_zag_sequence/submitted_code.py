"""
解説

- https://www.youtube.com/watch?v=8MAxgq6HieY
- https://www.youtube.com/watch?v=vMFEkSZ9lpw
- https://www.youtube.com/watch?v=Eyn-6YmXRjc
"""


def findZigZagSequence(a, n):
    a.sort()
    mid = int((n + 1) / 2) - 1  # インデックスは 0 から始まるため常に -1 する必要がある
    a[mid], a[n - 1] = a[n - 1], a[mid]
    # 1,2,3,7,5,6,4

    st = mid + 1
    ed = n - 2  #
    while st <= ed:
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1  #

    for i in range(n):
        if i == n - 1:
            print(a[i])
        else:
            print(a[i], end=" ")
    return


test_cases = int(input())
for cs in range(test_cases):
    n = int(input())
    a = list(map(int, input().split()))
    findZigZagSequence(a, n)
