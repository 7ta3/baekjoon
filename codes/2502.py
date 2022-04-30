D, K = map(int, input().split())

for i in range(1, K+1):
    for j in range(i, K+1):
        DP = [0] * D
        for k in range(D):
            if k == 0:
                DP[k] = i
            elif k == 1:
                DP[k] = j
            else:
                DP[k] = DP[k-1] + DP[k-2]
        if DP[-1] == K:
            print(i)
            print(j)
            exit(0)