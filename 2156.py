N = int(input())
lst = [0]
for _ in range(N):
    lst.append(int(input()))

dp = [0] * (N+1)

for i in range(1, N+1):
    if i == 1:
        dp[i] = lst[i]
    elif i == 2:
        dp[i] = lst[i-1] + lst[i]
    else:
        dp[i] = max(dp[i-2] + lst[i], dp[i-1], dp[i-3] + lst[i-1] + lst[i])
print(dp[-1])