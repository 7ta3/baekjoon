from collections import deque
N, K = map(int, input().split())
A = deque(list(map(int, input().split())))
Dead = 0
robots = deque([0] * N)
t = 0
while Dead < K:
    # 컨테이너 회전과 로봇 회전
    A.rotate(1)
    robots.rotate(1)
    robots[-1] = 0

    # 로봇 한 칸 회전
    for i in range(N-2, 0, -1):
        if robots[i] == 1 and robots[i+1] == 0 and A[i+1] > 0:
            robots[i+1] = 1
            robots[i] = 0
            A[i+1] -= 1
            if A[i+1] == 0:
                Dead += 1
    robots[-1] = 0

    # 로봇 추가
    if A[0] > 0:
        robots[0] = 1
        A[0] -= 1
        if A[0] == 0:
            Dead += 1
    t += 1
print(t)