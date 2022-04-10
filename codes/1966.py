from collections import deque
T = int(input())

for _ in range(T):
    N, M = map(int,input().split())
    important = deque(list(map(int,input().split())))
    lst = deque([i for i in range(0, N)])
    cnt = 0
    while True:
        if max(important) == important[0]:
            a = important.popleft()
            b = lst.popleft()
            cnt += 1
            if b == M :
                print(cnt)
                break
        else :
            a = important.popleft()
            important.append(a)
            b = lst.popleft()
            lst.append(b)
