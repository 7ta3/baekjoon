N = int(input())
P = [0] + list(map(int, input().split()))

DP = list(P)
for i in range(1, N+1):
    for j in range(i):
        DP[i] = max(DP[i], DP[i-j] + P[j])
print(DP[-1])