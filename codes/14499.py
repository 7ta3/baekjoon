from collections import deque
row_arr = deque([0, 0, 0, 0]) # 전개도상 row
col_arr = deque([0, 0, 0, 0]) # 전개도상 col

dx = [0, 1, -1, 0, 0] # 동 서 북 남
dy = [0, 0, 0, -1, 1] # 동 서 북 남

def roll(x, y, direction):
    x += dx[direction]
    y += dy[direction]
    if not(-1 < x < M and -1 < y < N): # 범위 벗어나면 주사위를 굴리지 않음
        return -1
    if direction == 1: # 동
        row_arr.rotate(1)
        col_arr[1] = row_arr[1]
        col_arr[3] = row_arr[3]
    elif direction == 2: # 서
        row_arr.rotate(-1)
        col_arr[1] = row_arr[1]
        col_arr[3] = row_arr[3]

    elif direction == 3: # 북
        col_arr.rotate(-1)
        row_arr[1] = col_arr[1]
        row_arr[3] = col_arr[3]

    elif direction == 4: # 남
        col_arr.rotate(1)
        row_arr[1] = col_arr[1]
        row_arr[3] = col_arr[3]
    return x, y
N, M, y, x, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))
D = list(map(int, input().split()))

for d in D:
    result = roll(x, y, d)
    if result == -1 : # 범위가 벗어나면 해당 경우는 그냥 pass
        continue
    else:
        x, y = result
        if arr[y][x] == 0: # 지도 좌표가 0이면 주사위 바닥면 숫자를 지도에 복사
            arr[y][x] = col_arr[-1]
        else : # 지도 좌표를 주사위 바닥면에 복사하고 지도는 0
            col_arr[-1] = arr[y][x]
            row_arr[-1] = arr[y][x]
            arr[y][x] = 0
        print(col_arr[1])
