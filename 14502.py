from itertools import combinations
import copy

N, M = map(int, input().split())
arr = []
V = []
lst = []
cnt_zeros = 0
for i in range(N):
    a = list(map(int, input().split()))
    for j in range(M):
        if a[j] == 2:
            V.append([j, i])
        if a[j] == 0:
            lst.append([j, i])
    arr.append(a)
# V : 바이러스 좌표 찾기, lst : 벽을 세울 수 있는 곳
cnt_zeros = len(lst)
a = list(combinations(lst, 3))
# 벽 세울 수 있는 모든 경우의 수

d = [(1,0), (-1,0), (0,1), (0,-1)]
cnt = 0
for border in a:
    temp_arr = copy.deepcopy(arr)
    ST = copy.deepcopy(V)
    temp_zeros = cnt_zeros
    for i in border:
        temp_zeros -= 1
        temp_arr[i[1]][i[0]] = 1
    # 벽 세우기
    while ST: # dfs
        s = ST.pop()
        for i in range(4):
            x = s[0] + d[i][0]
            y = s[1] + d[i][1]
            if -1 < x < M and -1 < y < N and temp_arr[y][x] == 0:
                ST.append([x, y])
                temp_arr[y][x] = 2
                temp_zeros -= 1
        if temp_zeros < cnt:
            temp_zeros = 0
            break
    cnt = max(temp_zeros, cnt)
print(cnt)