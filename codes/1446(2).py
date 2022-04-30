from collections import defaultdict
from heapq import *
N, D = map(int, input().split())

G = defaultdict(list)
for _ in range(N):
    S, E, P = map(int, input().split())
    G[S].append((S, E, P))

Dijkstra = [i for i in range(D+1)]
key = sorted(list(G.keys())) # 정렬 안 하면 바로 틀림

for i in key:
    Q = [i]
    while Q:
        e = heappop(Q)
        for start, end, path in G[e]:
            if end <= D and Dijkstra[start] + path < Dijkstra[end]:
                Dijkstra[end] = Dijkstra[start] + path
                heappush(Q, end)
                for j in range(end + 1, D + 1):
                    if Dijkstra[j - 1] + 1 < Dijkstra[j]:
                        Dijkstra[j] = Dijkstra[j - 1] + 1
print(Dijkstra[-1])