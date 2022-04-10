from collections import deque
import sys
N, M = map(int, sys.stdin.readline().split())

G = []
for _ in range(N):
    G.append(sys.stdin.readline().strip())

v = [[[-1, -1] for _ in range(M)] for _ in range(N)]
# [-1, -1] : 아직 여기에 온 적 없음
# [벽을 부순 적 없고 여기까지 왔을 때 거리, 벽을 부순 적 있고 여기까지 왔을 때 거리]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

ST = deque([[0, 0, 0]])
v[0][0] = [1, 0]
# [시작도 cnt하기로 했음, 벽인지 뭔지 확인 안 해도 됨]
while ST and v[N-1][M-1] == [-1, -1]:
    # 목적지에 도착하지 않았고 ST이 비어있지 않았다면
    s = ST.popleft()

    for i in range(4):
        nx = s[0] + dx[i]
        ny = s[1] + dy[i]
        if -1 < nx < M and -1 < ny < N:
            if G[ny][nx] == '1' and s[-1] == 0 and v[ny][nx][-1] == -1:
                # 벽인데 스택 넣을 때까지 벽을 부순 적 없고 전체를 봤을 때도 부수고 방문한 적 없을 때
                ST.append([nx, ny, 1])
                v[ny][nx][1] = v[s[1]][s[0]][0] + 1
                # 벽 부순 적 있다, 벽을 부순 적 없었던 지금까지 거리 + 1
            elif G[ny][nx] == '0' and v[ny][nx][s[-1]] == -1:
                # 길이고 전체를 봤을 때 방문한 적 없으면
                ST.append([nx, ny, s[-1]])
                v[ny][nx][s[-1]] = v[s[1]][s[0]][s[-1]] + 1
                # 부순 적 있든 없든 그 부분에 + 1
if v[-1][-1][0] == v[-1][-1][-1] == -1:
    print (-1)
elif v[-1][-1][0] == -1:
    print(v[-1][-1][-1])
else:
    print(v[-1][-1][0])


