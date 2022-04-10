N = int(input())
dp = [[0] * 10 for _ in range(N)]

for i in range(N):
    for j in range(10):
        if i == 0:
            dp[i][j] = 1
        else:
            if j == 0:
                dp[i][j] = dp[i-1][j+1]
            elif j == 9:
                dp[i][j] = dp[i-1][j-1]
            else :
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
print(sum(dp[-1][1:])%1000000000)