import sys
input = sys.stdin.readline

N = int(input())
L = []
for _ in range(N):
    L.append(list(map(int, input().split())))
L.sort(key=lambda x: x[0])

DP = [1] * N

for i in range(1, N):
    for j in range(i):
        if L[i][1] > L[j][1]:
            DP[i] = max(DP[i], DP[j] + 1)
print(N - max(DP))