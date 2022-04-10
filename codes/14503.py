N, M = map(int, input().split())
r, c, d = map(int, input().split())
dc = [0, 1, 0, -1]
dr = [-1, 0, 1, 0]

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
cnt = temp = 0
T = True

while T:
    if arr[r][c] == 0:
        cnt += 1
        arr[r][c] = 2

    while True:
        if temp == 4:
            nr = r - dr[d]
            nc = c - dc[d]
            if -1 < nr < N and -1 < nc < M and arr[nr][nc] != 1:
                r, c = nr, nc
                temp = 0
                break
            else:
                T = False
                break

        d = (d + 3) % 4
        nr = r + dr[d]
        nc = c + dc[d]

        if -1 < nr < N and -1 < nc < M and arr[nr][nc] == 0:
            r, c = nr, nc
            temp = 0
            break
        else:
            temp += 1
print(cnt)


