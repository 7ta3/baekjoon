from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    S = list(map(int, input().split()))
    G = []
    for _ in range(n):
        G.append(list(map(int, input().split())))
    E = list(map(int, input().split()))
    G.append(E)
    Q = deque([S])
    V = [False] * len(G)
    while Q:
        x, y = Q.popleft()
        if [x, y] == E:
            print('happy')
            break
        for idx, axis in enumerate(G):
            if not V[idx]:
                dx = abs(x-axis[0])
                dy = abs(y-axis[1])
                if dx + dy <= 1000:
                    Q.append(axis)
                    V[idx] = True
    else:
        print('sad')