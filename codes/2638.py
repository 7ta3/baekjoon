from collections import deque
N, M = map(int, input().split())
MAP = []
cheese = 0 # 치즈가 있는 칸의 수
for i in range(N):
    l = list(map(int, input().split()))
    for j in range(M):
        if l[j] == 1:
            cheese += 1
    MAP.append(l)

D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
F = [(0, 0), (M-1, 0), (0, N-1), (M-1, N-1)] # 공기와 접족된 칸을 체크 하기 위한 네 꼭짓점

t = 0
while True:
    V = [[False] * M for _ in range(N)]
    for i, j in F:
        V[j][i] = 0
        ST = deque([(i, j)])
        while ST:
            x, y = ST.popleft()
            for d in D:
                nx = x + d[0]
                ny = y + d[1]
                if -1 < ny < N and -1 < nx < M and not V[ny][nx]:
                    if MAP[ny][nx] == 0: # 공기
                        ST.append((nx, ny))
                        V[ny][nx] = True

                    elif MAP[ny][nx] == 1 and not V[ny][nx]: # 치즈 있는 칸 체크
                        V[ny][nx] = 1

                elif -1 < ny < N and -1 < nx < M and MAP[ny][nx] == 1 and V[ny][nx] == 1: # 치즈가 있다면 그 칸의 치즈는 녹는다
                    MAP[ny][nx] = 0
                    V[ny][nx] = True
                    cheese -= 1
    t += 1
    if cheese == 0:
        break
print(t)
