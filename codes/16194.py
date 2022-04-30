N = int(input())
L = [0] + list(map(int, input().split()))

DP = list(L)
for i in range(1, N+1):
    for j in range(i):
        DP[i] = min(DP[i-j]+DP[j], DP[i])
print(DP[N])
