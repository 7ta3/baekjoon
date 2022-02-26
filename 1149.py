N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (N+1) for _ in range(3)]
for i in range(1,N+1):
    dp[0][i] = min(dp[1][i-1], dp[2][i-1]) + lst[i-1][0]
    dp[1][i] = min(dp[0][i-1], dp[2][i-1]) + lst[i-1][1]
    dp[2][i] = min(dp[1][i-1], dp[0][i-1]) + lst[i-1][2]
print(min(dp[0][N], dp[1][N], dp[2][N]))