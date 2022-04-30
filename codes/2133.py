N = int(input())
DP = [0] * (N+1)
for i in range(2, N+1, 2):
    if i == 2:
        DP[i] = 3
    else:
        DP[i] = DP[i-2] * 3
        for j in range(0, i-2, 2):
            DP[i] += DP[j] * 2
        DP[i] += 2
print(DP[N])