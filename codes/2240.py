T, W = map(int, input().split())
DP = [0] * (W+1)
for i in range(1, T+1):
    A = int(input())
    for j in range(min(i, W), -1, -1):
        if (A == 1 and j % 2 == 0) or (A == 2 and j % 2):
            DP[j] += 1
        elif j < W and DP[j + 1] < DP[j] + 1:
            DP[j + 1] = DP[j] + 1
print(max(DP))