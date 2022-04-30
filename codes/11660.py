import sys
input = sys.stdin.readline

N, M = map(int, input().split())
G = []

for _ in range(N):
    G.append(list(map(int,input().split())))

DP = [[0] * (N+1) for _ in range(N+1)]
for y in range(N):
    for x in range(N):
        DP[y+1][x+1] = DP[y+1][x] + DP[y][x+1] - DP[y][x] + G[y][x]

for _ in range(M):
    y1, x1, y2, x2 = map(int, input().split())
    print(DP[y2][x2] - (DP[y1-1][x2] + DP[y2][x1-1] - DP[y1-1][x1-1]))