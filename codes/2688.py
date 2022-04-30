T = int(input())
for t in range(T):
    n = int(input())
    DP = [1] * 10
    for j in range(1, n+1):
        for i in range(1, 10):
            DP[i] += DP[i-1]
    print(DP[-1])

