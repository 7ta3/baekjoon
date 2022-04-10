from collections import deque
N, M = map(int, input().split())
G = []
for _ in range(N):
    G.append(list(map(int, input().split())))
D = [(1, 0), (0, 1)]

def cart():
    V = [[0] * M for _ in range(N)]
    V[0][0] = 1
    ST = deque([(0, 0, G[0][0])])

    while ST:
        x, y, B = ST.popleft()
        if x == M-1 and y == N-1:
            return V[y][x]-1

        for b in range(1, B+1):
            for d in D:
                nx = x + d[0] * b
                ny = y + d[1] * b
                if -1 < nx < M and -1 < ny < N and (not V[ny][nx] or V[ny][nx] > V[y][x] + 1):
                    V[ny][nx] = V[y][x] + 1
                    ST.append((nx, ny, G[ny][nx]))
print(cart())