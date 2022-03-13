from collections import deque
def move(D, S): # 비구름 움직이는 함수
    if D == 1:
        for i in range(N): RC[i].rotate(-S)
    elif D == 2:
        for i in range(N): RC[i].rotate(-S)
        RC.rotate(-S)
    elif D == 3:
        RC.rotate(-S)
    elif D == 4:
        for i in range(N): RC[i].rotate(S)
        RC.rotate(-S)
    elif D == 5:
        for i in range(N): RC[i].rotate(S)
    elif D == 6:
        for i in range(N): RC[i].rotate(S)
        RC.rotate(S)
    elif D == 7:
        RC.rotate(S)
    elif D == 8:
        for i in range(N): RC[i].rotate(-S)
        RC.rotate(S)

N, M = map(int, input().split())
baskets = deque([])
for _ in range(N):
    baskets.append(list(map(int, input().split())))

# 비바라기 시전
RC = deque([deque([0]) * N for _ in range(N)])
RC[-1][0] = 1
RC[-1][1] = 1
RC[-2][0] = 1
RC[-2][1] = 1

for _ in range(M):
    d, s = map(int, input().split())
    move(d, s)

    # 2. 각 구름에서 비가 내려
    for i in range(N):
        for j in range(N):
            if RC[j][i] == 1:
                baskets[j][i] += 1\

    # 4. 물복사 마법
    dx = [-1, -1, 1, 1]
    dy = [-1, 1, -1, 1]
    for i in range(N):
        for j in range(N):
            if RC[j][i] == 1:
                cnt = 0
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if -1 < nx < N and -1 < ny < N and baskets[ny][nx] > 0:
                        cnt += 1
                baskets[j][i] += cnt

    for i in range(N):
        for j in range(N):
            if baskets[j][i] >= 2 and not RC[j][i]: # 구름 생성
                RC[j][i] = 1
                baskets[j][i] -= 2
            else: # 구름 소멸
                RC[j][i] = 0

ans = 0
for i in range(N): ans += sum(baskets[i])
print(ans)