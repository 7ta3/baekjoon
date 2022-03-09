from collections import deque
M, N, H = map(int, input().split())
box = []
ST = deque([])
find_0 = False
for k in range(H):
    temp = []
    for i in range(N):
        a = list(map(int, input().split()))
        for j in range(M):
            if a[j] == 1:
                ST.append([j, i, k])
        if not find_0:
            if 0 in a:
                find_0 = True
        temp.append(a)
    box.append(temp)

dx = [-1, 1, 0, 0, 0, 0]
dy = [0, 0, 1, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

while ST:
    s = ST.popleft()
    for i in range(6):
        nx = s[0] + dx[i]
        ny = s[1] + dy[i]
        nz = s[2] + dz[i]

        if -1 < nx < M and -1 < ny < N and -1 < nz < H and not box[nz][ny][nx] :
            ST.append([nx, ny, nz])
            box[nz][ny][nx] = box[s[2]][s[1]][s[0]] + 1

max_val = 0
for i in range(H):
    for j in range(N):
        if find_0 == False:
            print(0)
            exit(0)
        elif 0 in box[i][j]:
            print(-1)
            exit(0)
        else :
            max_val = max(max(box[i][j]), max_val)
else:
    print(max_val-1)