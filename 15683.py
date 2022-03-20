import copy

N, M = map(int, input().split())

G = []
cctv = []
zeros = 0
D = [[],
     [[[0, -1]], [[-1, 0]], [[0, 1]], [[1, 0]]],
     [[[-1, 0], [1, 0]], [[0, -1], [0, 1]]],
     [[[1, 0],[0, -1]], [[-1, 0],[0, -1]], [[1, 0],[0, 1]], [[-1, 0],[0, 1]]],
     [[[-1, 0],[0, -1],[1, 0]], [[0, 1],[1, 0],[0, -1]], [[-1, 0],[1, 0],[0, 1]], [[-1, 0],[0, 1],[0, -1]]],
     [[[-1, 0],[0, -1],[1, 0],[0, 1]]]]
# D[i] : i번 CCTV가 감시할 수 있는 방향의 모든 경우의 수 (x, y)

def CCTV(idx, tmp_G):
    if idx > cctv_num - 1:
        global cnt_zeros
        temp = 0
        for i in range(N):
            temp += tmp_G[i].count(0)
        if cnt_zeros > temp:
            cnt_zeros = temp
        return
    # temp : cctv의 감시 방향을 정하고 해당 방향을 살펴봤을 때, 최종적으로 남은 사각지대의 수

    for i in D[cctv[idx][-1]]:
        temp_G = copy.deepcopy(tmp_G)
        for d in i:
            x, y = cctv[idx][0], cctv[idx][1]
            nx = x + d[0]
            ny = y + d[1]
            while -1 < nx < M and -1 < ny < N and temp_G[ny][nx] != 6:
                temp_G[ny][nx] = 7
                nx = nx + d[0]
                ny = ny + d[1]
        CCTV(idx+1, temp_G)
        # 하나의 CCTV에 대해서 방향을 선택하고 감시 범위를 체크하고 다음 CCTV로 넘어가는 것을 모든 경우의 수에 대해 진행

cctv_num = 0
cnt_zeros = 0
for i in range(N):
    g = list(map(int, input().split()))
    G.append(g)
    for j in range(M):
        if (g[j] != 0) and (g[j] != 6):
            cctv.append([j, i, g[j]])
            cctv_num += 1
        elif g[j] == 0:
            cnt_zeros += 1

CCTV(0, G)
print(cnt_zeros)