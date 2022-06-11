N, M = map(int, input().split())
G = [[0] * 301 for _ in range(301)]

for _ in range(N):
    x, y = map(int, input().split())
    G[y][x] = 1

DP = [[0] * 301 for _ in range(301)]
for y in range(301):
    for x in range(301):
        if x == 0:
            DP[y][x] = DP[y-1][x]
        elif y == 0:
            DP[y][x] = DP[y][x-1]
        else:
            DP[y][x] = max(DP[y-1][x], DP[y][x-1])
        if G[y][x]:
            DP[y][x] += max(0, M - x - y)
print(DP[-1][-1])