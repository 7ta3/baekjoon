from collections import defaultdict
import sys
input = sys.stdin.readline
INF = sys.maxsize

def dfs(n1, s, c, B, C):
    if n1 == B:
        global ans
        ans = min(ans, c)
        return

    for cost, n2 in G[n1]:
        if not V[n2] and s + cost <= C:
            V[n2] = True
            dfs(n2, s + cost, max(c, cost), B, C)
            V[n2] = False

N, M, A, B, C = map(int, input().split())
G = defaultdict(list)
for _ in range(M):
    n1, n2, cost = map(int, input().split())
    G[n1].append((cost, n2))
    G[n2].append((cost, n1))

V = [False] * (N+1)
ans = INF
dfs(A, 0, 0, B, C)

if ans == INF:
    print(-1)
else:
    print(ans)