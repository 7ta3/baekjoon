n = int(input())
lst = list(map(int, input().split()))
dp = [0] * n
for i in range(n):
    if i == 0:
        dp[i] = lst[i]
    else:
        if dp[i-1] + lst[i] > 0:
            dp[i] = max(dp[i-1] + lst[i], lst[i])
        else:
            dp[i] = lst[i]
print(max(dp))
