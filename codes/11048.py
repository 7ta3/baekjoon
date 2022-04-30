N, M = map(int,input().split())
G = []
for _ in range(N):
    G.append(list(map(int, input().split())))

DP = [[0] * M for _ in range(N)]
for y in range(N):
    for x in range(M):
        if x == y == 0:
            DP[y][x] = G[y][x]
        elif x == 0:
            DP[y][x] = DP[y-1][x] + G[y][x]
        elif y == 0:
            DP[y][x] = DP[y][x-1] + G[y][x]
        else:
            DP[y][x] = max(DP[y-1][x-1], DP[y-1][x], DP[y][x-1]) + G[y][x]

print(DP[-1][-1])