T = int(input())
DP = [1] * 10001
for j in range(2, 4):
    for i in range(j, 10001):
        DP[i] += DP[i-j]

for t in range(T):
    n = int(input())
    print(DP[n])