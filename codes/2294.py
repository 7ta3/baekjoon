n, k = map(int, input().split())
C = set()
for _ in range(n):
    A = int(input())
    if A <= k: C.add(A)
C = sorted(list(C))

DP = [-1] * (k+1)
for i in range(k+1):
    if i == 0:
        DP[i] = 0
    elif i in C:
        DP[i] = 1
    else:
        for j in C:
            if DP[i-j] != -1:
                if DP[i] == -1:
                    DP[i] = DP[i-j] + 1
                else:
                    DP[i] = min(DP[i], DP[i-j] + 1)
print(DP[-1])