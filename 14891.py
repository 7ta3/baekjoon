import pprint
arr = [list(input()) for _ in range(4)]

def turn(N, D):
    if D == 1: # 시계방향
        temp = arr[N].pop()
        arr[N].insert(0, temp)
    else: # 반시계방향
        temp = arr[N].pop(0)
        arr[N].append(temp)
# 선택된 톱니바퀴 N을 D방향으로 회전하는 함수

def neighbor(N, D, X): # 이웃 톱니 바퀴와 닿아있는 부분이 다르면 회전할 예정이므로 그 톱니의 이웃 톱니 바퀴도 살펴보고 본인은 회전
    if X == 2: # 양쪽 이웃 톱니바퀴 확인
        if -1 < N-1 < 4:
            if arr[N-1][2] != arr[N][6]:
                neighbor(N-1, -D, 0)
                turn(N-1, -D)
        if -1 < N+1 < 4:
            if arr[N+1][6] != arr[N][2]:
                neighbor(N+1, -D, 1)
                turn(N+1, -D)
    elif X == 1 : # 오른쪽 톱니바퀴만 확인
        if -1 < N+1 < 4:
            if arr[N+1][6] != arr[N][2]:
                neighbor(N+1, -D, 1)
                turn(N+1, -D)
    elif X == 0: # 왼쪽 톱니바퀴만 확인
        if -1 < N-1 < 4:
            if arr[N-1][2] != arr[N][6]:
                neighbor(N-1, -D, 0)
                turn(N-1, -D)

K = int(input())
for k in range(K):
    a, b = map(int, input().split())
    a -= 1
    neighbor(a, b, 2)
    turn(a, b) # neighbor은 이웃 톱니 바퀴만 회전시키므로 시작 톱니 바퀴도 회전

ans = 0
for i in range(4): # 점수 계산
    if arr[i][0] == '1':
        ans += 2 ** i
print(ans)
