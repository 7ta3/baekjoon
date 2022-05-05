import sys
input =sys.stdin.readline
INF = sys.maxsize

N, M, K = map(int, input().split())
A = [0]
for _ in range(N):
    A.append(int(input()))

DP = [0] * (N+1)
DP[1] = K
for i in range(2, N+1):
    maxV = minV = A[i]
    DP[i] = DP[i-1] + K
    R = min(i, M)
    for s in range(1, R):
        maxV = max(maxV, A[i - s])
        minV = min(minV, A[i - s])
        DP[i] = min(DP[i - s - 1] + K + (s + 1) * (maxV - minV), DP[i])
print(DP[-1])