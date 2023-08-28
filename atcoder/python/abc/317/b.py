N = int(input())
A = list(map(int, input().split()))
A.sort()
all = [i for i in range(A[0], A[len(A) - 1])]
print(list(set(all) - set(A))[0])
