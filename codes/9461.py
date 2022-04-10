T = int(input())

for _ in range(T):
    N = int(input())
    dp = [0] *(N+1)
    for i in range(1, N+1):
        if i == 1 or i == 2 or i == 3:
            dp[i] = 1
        else:
            dp[i] = dp[i-2] + dp[i-3]
    print(dp[N])