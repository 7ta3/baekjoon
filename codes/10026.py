from collections import deque
N = int(input())
D = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def bfs(x, y, M):
    val = M[y][x]
    ST = deque([(x, y)])
    while ST:
        x, y = ST.popleft()
        for d in D:
            nx = x + d[0]
            ny = y + d[1]
            if -1 < nx < N and -1 < ny < N and M[ny][nx] == val and not V[ny][nx]:
                ST.append((nx, ny))
                V[ny][nx] = True

GG = [] # 적록색맹이 아닌 경우
G = [] # 적록색맹인 경우
for _ in range(N):
    l = list(input())
    GG.append(list(l))
    for j in range(N):
        if l[j] == 'R' or l[j] == 'G':
            l[j] = 1
        else:
            l[j] = 0
    G.append(list(l))

# 적록색맹이 아닌 경우 계산
V = [[False] * N for _ in range(N)]
ans1 = 0
for i in range(N):
    for j in range(N):
        if V[j][i]:
            continue
        ans1 += 1
        bfs(i, j, GG)

# 적록색맹인 경우 계산
V = [[False] * N for _ in range(N)]
ans2 = 0
for i in range(N):
    for j in range(N):
        if V[j][i]:
            continue
        ans2 += 1
        bfs(i, j, G)
print(ans1, ans2)