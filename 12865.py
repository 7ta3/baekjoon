N, K = map(int, input().split())
arr = [[0, 0]]
dp = [[0 for _ in range(K+1)] for _ in range(N+1)]
for _ in range(N):
    arr.append(list(map(int, input().split())))
for i in range(1, N+1):
    for j in range(1, K+1):
        if j < arr[i][0]:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(arr[i][1] + dp[i-1][j-arr[i][0]], dp[i-1][j])
print(dp[N][K])
