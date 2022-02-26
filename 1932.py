N = int(input())
lst = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*i for i in range(1, N+1)]
for i in range(N-1,-1,-1):
    for j in range(i+1):
        if i == N-1 :
            dp[i][j] = lst[i][j]
        else:
            dp[i][j] = max(dp[i+1][j], dp[i+1][j+1]) + lst[i][j]
print(dp[0][0])