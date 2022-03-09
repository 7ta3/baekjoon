from collections import deque
M, N = map(int, input().split())
box = []
ST = deque([])
find_0 = False
for i in range(N):
    a = list(map(int, input().split()))
    for j in range(M):
        if a[j] == 1:
            ST.append([j, i])
    if not find_0:
        if 0 in a:
            find_0 = True

    box.append(a)
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

while ST:
    s = ST.popleft()
    for i in range(4):
        nx = s[0] + dx[i]
        ny = s[1] + dy[i]

        if -1 < nx < M and -1 < ny < N and not box[ny][nx] :
            ST.append([nx, ny])
            box[ny][nx] = box[s[1]][s[0]] + 1

max_val = 0
for i in range(N):
    if find_0 == False:
        print(0)
        break
    elif 0 in box[i]:
        print(-1)
        break
    else :
        max_val = max(max(box[i]), max_val)
else:
    print(max_val-1)