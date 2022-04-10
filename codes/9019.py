from collections import deque

def bfs(S, E):
    V = [False] * 10000
    V[S] = True
    ST = deque([(S, '')])
    while ST:
        num, s = ST.popleft()
        if num == E:
            return s
        temp = (2 * num) % 10000
        if not V[temp]:
            V[temp] = True
            ST.append((temp, s+'D'))
        temp = num - 1 if num != 0 else 9999
        if not V[temp]:
            V[temp] = True
            ST.append((temp, s+'S'))
        temp = (num % 1000) * 10 + num // 1000
        if not V[temp]:
            V[temp] = True
            ST.append((temp, s+'L'))
        temp = (num % 10) * 1000 + (num // 10)
        if not V[temp]:
            V[temp] = True
            ST.append((temp, s+'R'))

T = int(input())
for _ in range(T):
    S, E = map(int, input().split())
    print(bfs(S, E))