from collections import deque
N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for i in range(M):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
visited = [False] * (N+1)
cnt = 0

for i in range(1, N+1):
    if not visited[i]:
        ST = deque([i])
        visited[i] = True
        while ST:
            s = ST.popleft()
            for i in G[s]:
                if not visited[i]:
                    ST.append(i)
                    visited[i] = True
        cnt += 1
print(cnt)

