from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
G = []
for _ in range(N):
    G.append(list(map(int, input().split())))

t = 0
D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while True:
    V = [[0] * M for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(M):
            if not V[i][j] and G[i][j]:
                cnt += 1
                Q = deque([(j, i)])
                V[i][j] = True
                while Q:
                    x, y = Q.popleft()
                    for d in D:
                        nx = x + d[0]
                        ny = y + d[1]
                        if -1 < nx < M and -1 < ny < N and not V[ny][nx]:
                            if not G[ny][nx]:
                                G[y][x] = max(0, G[y][x] - 1)
                            elif G[ny][nx]:
                                Q.append((nx, ny))
                                V[ny][nx] = True
    if cnt >= 2:
        print(t)
        break
    elif cnt == 0:
        print(0)
        break
    t += 1