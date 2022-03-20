import copy

R, C, T = map(int, input().split())
A = []
AC = [] # 공기청정기
for i in range(R):
    a = list(map(int, input().split()))
    if a[0] == -1 :
        AC.append(i)
    A.append(a)

D = [(-1, 0), (0, -1), (0, 1), (1, 0)]
for _ in range(T):
    temp_A = [[0] * C for _ in range(R)]
    temp_A[AC[0]][0] = -1
    temp_A[AC[1]][0] = -1
    for i in range(C):
        for j in range(R):
            if A[j][i] > 0 :
                temp = 0
                for d in D:
                    nx = i + d[0]
                    ny = j + d[1]
                    if -1 < nx < C and -1 < ny < R and A[ny][nx] >=0:
                        temp += 1
                        temp_A[ny][nx] += A[j][i] // 5
                temp_A[j][i] += A[j][i] - (A[j][i] // 5) * temp
    A = copy.deepcopy(temp_A)
    # 미세먼지 확산
    for i in range(AC[0]-1, 0, -1):
        A[i][0] = A[i-1][0]
    for i in range(C-1):
        A[0][i] = A[0][i+1]
    for i in range(AC[0]):
        A[i][-1] = A[i+1][-1]
    for i in range(C-1, 0, -1):
        if i-1 == 0:
            A[AC[0]][i] = 0
        else:
            A[AC[0]][i] = A[AC[0]][i-1]
    # 위쪽 반시계방향

    for i in range(AC[1]+1, R-1):
        A[i][0] = A[i+1][0]
    for i in range(C-1):
        A[-1][i] = A[-1][i+1]
    for i in range(R-1, AC[1], -1):
        A[i][-1] = A[i-1][-1]
    for i in range(C-1,0,-1):
        if i-1 == 0:
            A[AC[1]][i] = 0
        else:
            A[AC[1]][i] = A[AC[1]][i-1]
    # 아래쪽 시계방향
    # 공기 청정기 작동
ans = 2
for i in range(C):
    for j in range(R):
        ans += A[j][i]
print(ans)
