import sys
input = sys.stdin.readline
INF = sys.maxsize
t = 1
D = [(-1, 0), (-1, -1), (0, -1), (1, -1)]
while True:
    N = int(input())
    if N == 0:
        break

    G = []
    for _ in range(N):
        G.append(list(map(int, input().split())))

    DP = [[INF] * 3 for _ in range(N)]
    for y in range(N):
        for x in range(3):
            if x == 0 and y == 0:
                continue

            for d in D:
                nx = x + d[0]
                ny = y + d[1]
                if -1 < nx < 3 and -1 < ny < N:
                    DP[y][x] = min(DP[y][x], DP[ny][nx])

            if DP[y][x] == INF:
                DP[y][x] = 0

            DP[y][x] += G[y][x]

    print('%d.'%t, DP[-1][1])
    t += 1

