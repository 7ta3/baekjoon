from collections import deque
def chk(val):
    if val == 1:
        return 2
    elif val == 2:
        return 1

T = int(input())
for _ in range(T):
    V, E = map(int, input().split())
    G = [[] for _ in range(V+1)]
    for _ in range(E):
        u, v = map(int, input().split())
        G[u].append(v)
        G[v].append(u)

    ans = True
    visited = [0] * (V+1)
    for i in range(1, V+1):
        ST = deque([i])
        if visited[i] == 0:
            visited[i] = 1
        while ST and ans:
            s = ST.popleft()
            for j in G[s]:
                if visited[j] == 0:
                    visited[j] = chk(visited[s])
                    ST.append(j)
                elif visited[j] != chk(visited[s]):
                    ans = False
    if ans:
        print('YES')
    else:
        print('NO')