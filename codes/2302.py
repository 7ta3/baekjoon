N = int(input())
M = int(input())
L = []
for _ in range(M):
    L.append(int(input()))

DP = [0] * (N+1)
for i in range(N+1):
    if i == 0 or i == 1:
        DP[i] = 1
    elif (i not in L) and (i - 1 not in L):
        DP[i] += DP[i-1] + DP[i-2]
    else:
        DP[i] = DP[i-1]
print(DP[-1])