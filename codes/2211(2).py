from heapq import *
from collections import defaultdict
import sys
input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
G = defaultdict(list)
for _ in range(M):
    A, B, C = map(int, input().split())
    G[A].append((C, B))
    G[B].append((C, A))

V = [False] * (N+1)
D = [INF] * (N+1)
D[1] = 0
Q = [(0, 1)]

while Q:
    c, n1 = heappop(Q)

    for cost, n2 in G[n1]:
        if c + cost < D[n2]:
            V[n2], D[n2] = n1, c + cost
            heappush(Q, (c + cost, n2))

print(N-1)
for i in range(2, N+1):
    print(i, V[i])