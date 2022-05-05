from collections import defaultdict
import sys
from heapq import *
input = sys.stdin.readline
INF = sys.maxsize

def dijkstra():
    D = [[INF] * (N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        Q = [(0, i)]
        D[i][i] = 0
        while Q:
            c, n1 = heappop(Q)
            for cost, n2 in G[n1]:
                if cost + c < D[i][n2]:
                    D[i][n2] = cost + c
                    heappush(Q, (cost + c, n2))
    return D

N, M, X = map(int, input().split())
G = defaultdict(list)
for _ in range(M):
    A, B, T = map(int, input().split())
    G[A].append((T, B))

ans = 0
D = dijkstra()
for i in range(1, N+1):
    ans = max(ans, D[i][X] + D[X][i])
print(ans)


