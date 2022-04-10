N = int(input())
M = []
D = [(0, -1), (-1, 0), (1, 0), (0, 1)] # 상 좌 우 하

for i in range(N):
    l = list(map(int, input().split()))
    for j in range(N): # 상어 위치 체크하고 해당 위치 0
        if l[j] == 9:
            B = (j, i)
            l[j] = 0
    M.append(l)

ST =[(B[0], B[1], 0)]
size = 2
size_cnt = 0 # 현재 사이즈에서 잡아먹은 물고기의 수
t = 0
V = [[False] * N for _ in range(N)]
V[B[1]][B[0]] = True

while ST:
    ST.sort(key=lambda x: (x[2], x[1], x[0]))
    # 가까운 곳 > 위쪽 > 왼쪽이 우선 순위이므로 정렬

    x, y, cnt = ST.pop(0)
    # 현재 x / 현재 y / 여기까지 오는 데 걸리는 시간

    if 0 < M[y][x] < size:
        t += cnt
        size_cnt += 1
        if size_cnt == size:
            size += 1
            size_cnt = 0
        M[y][x] = 0
        ST = [(x, y, 0)]
        V = [[False] * N for _ in range(N)]
        continue
    # 해당 위치에 잡아먹을 수 있는 물고기가 있는 경우

    for d in D:
        nx = x + d[0]
        ny = y + d[1]
        if -1 < nx < N and -1 < ny < N and not V[ny][nx] and M[ny][nx] <= size:
            V[ny][nx] = True
            ST.append((nx, ny, cnt + 1))
    # 갈 수 있으면 일단 ST에 넣기
print(t)
