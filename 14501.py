N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dp = [0] * (N+1)
for i in range(N-1, -1, -1):
    T, P = arr[i][0], arr[i][1]
    if T + i > N:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+T] + P, dp[i+1])
print(dp[0])


