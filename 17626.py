import math
N = int(input())

dp = [0] * (N+1)
for i in range(1, N+1):
    j = int(math.sqrt(i))
    if i == 1 :
        dp[i] = 1
    elif j*j == i :
        dp[i] = 1
    else :
        dp[i] = dp[i-1]+1
        for k in range(1, j+1):
            dp[i] = min(dp[i], dp[k*k]+dp[i-k*k])
print(dp[-1])