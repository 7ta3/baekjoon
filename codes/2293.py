n, k = map(int, input().split())
C = []
for _ in range(n):
    C.append(int(input()))

DP = [0] * (k+1)
DP[0] = 1
for i in range(n):
    for j in range(C[i], k+1):
        DP[j] += DP[j-C[i]]
print(DP[k])