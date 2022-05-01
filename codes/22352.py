from collections import deque
N, M = map(int, input().split())
prev = []
for _ in range(N):
    prev.append(list(map(int, input().split())))

pres = []
for _ in range(N):
    pres.append(list(map(int, input().split())))

D = [(1, 0), (-1, 0), (0, -1), (0, 1)]
def bfs():
    ans = 0
    flag = False
    V = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if not V[i][j]:
                ans += 1
                val1 = prev[i][j]
                val2 = pres[i][j]

                if val1 != val2 and flag:
                    print('NO')
                    return
                elif val1 != val2 and not flag:
                    flag = True

                Q = deque([(j, i)])
                while Q:
                    x, y = Q.popleft()
                    for d in D:
                        nx = x + d[0]
                        ny = y + d[1]
                        if -1 < ny < N and -1 < nx < M and not V[ny][nx]:
                            if prev[ny][nx] == val1 and pres[ny][nx] == val2:
                                V[ny][nx] = True
                                Q.append((nx, ny))

                            elif (prev[ny][nx] == val1 and pres[ny][nx] != val2):
                                print('NO')
                                return
    print('YES')
bfs()