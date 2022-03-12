from collections import deque
N = int(input())
board = [[1] * (N+2)]
for _ in range(N): board.append([1] + [0]*N + [1])
board.append([1] * (N+2))

K = int(input())
for _ in range(K):
    R, C = map(int, input().split())
    board[R][C] = 2
# 사과는 board에 2로 표기

L = int(input())
lst = []
for i in range(L):
    X, C = input().split()
    X = int(X)
    lst.append([X, C])

D = [(1,0), (0,1), (-1,0), (0,-1)] # 시계 방향
d = 0

x, y = 1, 1
# 머리 부분
ST = deque([[1, 1]])
# 뱀이 차지하고 있는 부분 ST[0]는 꼬리, ST[-1]은 머리
board[y][x] = 5
# 현재 뱀 몸이 차지하는 부분은 board에 5로 표기
t = 1

while True:
    x += D[d][0]
    y += D[d][1]

    if board[y][x] == 1 or board[y][x] == 5:
        break
    # 벽이거나 몸이면 break

    ST.append([x, y])
    if board[y][x] == 0:
        a = ST.popleft()
        board[a[1]][a[0]] = 0
    # 사과가 없으면 몸통 길이 유지

    if lst and t == lst[0][0]:
    # 방향 바꾸기
        if lst[0][1] == 'L':
            d = (d + 3) % 4
        elif lst[0][1] == 'D':
            d = (d + 1) % 4
        lst.pop(0)
    board[y][x] = 5
    t += 1
print(t)


