import copy
from collections import deque
N, Q = map(int, input().split())
def turn(L): # 90도 회전
    global A
    arr = [[0] * 2**N for _ in range(2**N)]
    NN = 2**(N-L)
    for i in range(NN):
        for j in range(NN):
            for y in range(2**L):
                for x in range(2**L):
                    arr[(2**L)*i+x][((2**L)*(j+1)-1)-y] = A[(2**L)*i+y][(2**L)*j+x]
    A = copy.deepcopy(arr)

def fire(): # 얼음이 있는 칸 3개 또는 그 이상과 인접해있지 않으면 얼음의 양 1 감소
    global A
    arr = [[0] * 2**N for _ in range(2**N)]
    for y in range(2**N):
        for x in range(2**N):
            if A[y][x] == 0:
                continue
            cnt = 0
            for d in D:
                nx = x + d[0]
                ny = y + d[1]
                if -1 < nx < 2**N and -1 < ny < 2**N and A[ny][nx] != 0:
                    cnt += 1
            if cnt >= 3:
                arr[y][x] = A[y][x]
            else:
                arr[y][x] = A[y][x] - 1
    A = copy.deepcopy(arr)

D = [(-1,0), (1,0), (0,-1), (0,1)]
A = []
for _ in range(2**N):
    A.append(list(map(int, input().split())))
L = list(map(int, input().split()))
for i in L:
    turn(i)
    fire()

ice = 0
for i in range(2**N):
    ice += sum(A[i])

# 가장 큰 땅 덩어리 찾기 (BFS)
land = 0
V = [[False] * (2**N) for _ in range(2**N)]
for i in range(2**N):
    for j in range(2**N):
        if not V[j][i] and A[j][i]:
            ST = deque([(i, j)])
            V[j][i] = True
            temp_land = 1
            while ST:
                x, y = ST.popleft()
                for d in D:
                    nx = x + d[0]
                    ny = y + d[1]
                    if -1 < nx < 2**N and -1 < ny < 2**N and not V[ny][nx] and A[ny][nx]:
                        temp_land += 1
                        V[ny][nx] = True
                        ST.append((nx, ny))
            land = max(land, temp_land)
print(ice)
print(land)