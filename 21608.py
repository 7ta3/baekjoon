N = int(input())
arr = [[0] * N for _ in range(N)]
axis = {}
friend = {}
def chk_friends(x, friends, cnt, null, position):
    for i in [(0,-1),(-1,0),(1,0),(0,1)]: # 친구 좌표 기준으로 상하좌우의 빈 공간에 대해 가치 판단
        nx = x[0] + i[0]
        ny = x[1] + i[1]
        if -1 < nx < N and -1 < ny < N and arr[ny][nx] == 0:
            temp_cnt = 0
            temp_null = 0
            for j in [(0,-1),(-1,0),(1,0),(0,1)]:
                nx2 = nx + j[0]
                ny2 = ny + j[1]
                if -1 < nx2 < N and -1 < ny2 < N and arr[ny2][nx2] in friends: # 친구가 있으면 temp_cnt 증가
                    temp_cnt += 1
                if -1 < nx2 < N and -1 < ny2 < N and arr[ny2][nx2] == 0: # 빈공간이 있으면 temp_null 증가
                    temp_null += 1
            if cnt < temp_cnt : # 친구가 더 많으면
                cnt, null, position = temp_cnt, temp_null, [nx, ny]
            if cnt == temp_cnt and temp_null > null: # 친구는 같은데 빈공간이 더 많으면
                null, position = temp_null, [nx, ny]
            elif cnt == temp_cnt and temp_null == null: # 빈공간도 같은데
                if position[1] > ny: # 행 기준으로 더 작으면
                    position = [nx, ny]
                elif position[1] == ny and position[0] > nx: # 행도 같은데 열 기준으로 더 작으면
                    position = [nx, ny]

    return cnt, null, position

def chk_around(): # 비어있는 곳이 제일 많은 곳을 기준으로 현재 위치 초기화
    cnt = 0
    pos = [-1, -1]
    temp_chk = False
    for y in range(N):
        for x in range(N):
            if arr[y][x] != 0 :
                continue
            elif temp_chk == False:  # 처음 만나는 빈 공간에 pos 초기화
                pos = [x, y]
                temp_chk = True
            temp = 0
            for j in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                nx = x + j[0]
                ny = y + j[1]
                if -1 < nx < N and -1 < ny < N and arr[ny][nx] == 0:
                    temp += 1
            if temp > cnt:
                cnt = temp
                pos = [x, y]
            if cnt == 4:
                return pos
    return pos

for _ in range(N*N):
    a = list(map(int, input().split()))
    N_num, N_list = a[0], a[1:]
    keys = list(axis.keys())
    N_pos, N_cnt, N_null = chk_around(), 0, 0 # 일단 현재 좌표에 대해서 빈 공간으로 초기화
    chk = False
    for i in N_list:
        if i in keys: # 친구가 이미 배정받았으면 친구를 기준으로 판단
            c, n, p = chk_friends(axis[i], N_list, N_cnt, N_null, N_pos)
            if c > N_cnt:
                N_cnt, N_pos, N_null = c, p, n
            elif c == N_cnt and n > N_null:
                N_pos, N_null = p, n
            elif c == N_cnt and n == N_null and N_pos[1] > p[1]:
                N_pos = p
            elif c == N_cnt and n == N_null and N_pos[0] > p[0]:
                N_pos = p
    axis[N_num] = N_pos
    friend[N_num] = N_list
    arr[N_pos[1]][N_pos[0]] = N_num
ans = 0
for i in range(N):
    for j in range(N):
        temp = 0
        for k in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
            nx = i + k[0]
            ny = j + k[1]
            if -1 < nx < N and -1 < ny < N:
                if arr[ny][nx] in friend[arr[j][i]]:
                    temp += 1
        # 주변의 친구 수에 따라 0 10 100 1000으로 점수 부여
        if temp == 0: pass
        else:
            ans += 10 ** (temp-1)
print(ans)