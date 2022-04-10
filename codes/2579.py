N = int(input())
stairs = [0]
for _ in range(N):
    stairs.append(int(input()))
dp = [0] * (N+1)
for i in range(1, N+1):
    if i == 1:
        dp[i] = stairs[i]
    else:
        dp[i] = max(dp[i-3] + stairs[i-1] + stairs[i], dp[i-2] + stairs[i])
print(dp[N])