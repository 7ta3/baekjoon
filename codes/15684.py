N, M, H = map(int, input().split())
arr = [[0] * H for _ in range(N-1)]
for _ in range(M):
    a, b = map(int, input().split())
    arr[b-1][a-1] = 1
dx = [-1, 1, 0]
dy = [0, 0, 1]

def exploration(idx): # 도착점 찾는 함수
    for i in range(H):
        if -1 < idx-2 < N-1 and arr[idx-2][i] == 1:
            idx -= 1
            continue
        if -1 < idx - 1 < N-1 and arr[idx-1][i] == 1:
            idx += 1
    return idx

def chk(): # 사다리가 자기 번호로 돌아가는지 확인
    for i in range(1, N + 1):
        if exploration(i) != i:
            return False
    else:
        return True

def ladder1(cnt, start_i): # 사다리 하나
    for i in range(start_i, H):
        for j in range(N - 1):
            if j+1 < N-1 and arr[j+1][i]: continue
            if -1 < j-1 and arr[j-1][i]: continue
            if arr[j][i]: continue
            arr[j][i] = 1
            chk()
            if chk():
                print(cnt)
                exit(0)
            arr[j][i] = 0

def ladder2(cnt,start_i): # 사다리 둘
    for i in range(start_i, H):
        for j in range(N - 1):
            if j+1 < N-1 and arr[j+1][i]: continue
            if -1 < j-1 and arr[j-1][i]: continue
            if arr[j][i]: continue
            arr[j][i] = 1
            ladder1(cnt, i)
            arr[j][i] = 0

def ladder3(cnt): # 사다리 셋
    for i in range(H):
        for j in range(N - 1):
            if j+1 < N-1 and arr[j+1][i]: continue
            if -1 < j-1 and arr[j-1][i]: continue
            if arr[j][i]: continue
            arr[j][i] = 1
            ladder2(cnt, i)
            arr[j][i] = 0

cnt = 0
if chk():
    print(cnt)
    exit(0)
cnt = 1
ladder1(1, 0)
ladder2(2, 0)
ladder3(3)
print(-1)