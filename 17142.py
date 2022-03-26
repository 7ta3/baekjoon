from itertools import combinations
import copy
from collections import deque

N, M = map(int, input().split())
G = []
Virus = []
zeros = 0
for i in range(N):
    line = list(map(int, input().split()))
    for j in range(N):
        if line[j] == 2:
            Virus.append([j, i])
        if line[j] == 0:
            zeros += 1
    G.append(line)

D = [(-1,0), (1,0), (0,-1), (0,1)]

case = list(combinations(Virus, M)) # 활성화 시킬 바이러스
min_t = 10**10

for c in case:
    arr = copy.deepcopy(G)
    ST = deque([])
    zero = zeros
    t = -1

    for i in c:
        ST.append([i[0], i[1], 0])
        arr[i[1]][i[0]] = 3

    while ST and zero > 0:
        x, y, t = ST.popleft()
        for d in D:
            nx = x + d[0]
            ny = y + d[1]
            if - 1 < nx < N and -1 < ny < N and (arr[ny][nx] == 0 or arr[ny][nx] == 2):
                if arr[ny][nx] == 0 :
                    zero -= 1
                ST.append((nx, ny, t+1))
                arr[ny][nx] = 3
    if zero == 0:
        min_t = min(min_t, t+1)

if min_t == 10**10:
    print(-1)
else:
    print(min_t)


