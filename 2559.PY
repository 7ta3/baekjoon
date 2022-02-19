import sys
N, K = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
val = 0
for i in range(K):
    val += lst[i]
max_val = val

for i in range(K, N):
    val = val + lst[i] - lst[i-K]
    max_val = max(val, max_val)
print(max_val)