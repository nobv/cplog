N, H, X = list(map(int, input().split()))
P = list(map(int, input().split()))
print(min([i for i, p in enumerate(P) if (H + p) >= X]) + 1)
