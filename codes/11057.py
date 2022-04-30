N = int(input())

DP = [1] * 10
for i in range(1, N):
    for j in range(9, 0, -1):
        DP[j] = (sum(DP[:j]) + DP[j]) % 10_007
print(sum(DP))
