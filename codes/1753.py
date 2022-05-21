import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize
V, E = map(int, input().split())
G = [[] for _ in range(V+1)]
K = int(input())

for _ in range(E):
    u, v, w = map(int, input().split())
    G[u].append((w, v))

Q = [(0, K)]
D = [INF] * (V+1)
D[K] = 0
while Q:
    w, n1 = heapq.heappop(Q)

    if D[n1] < w:
        continue

    for weight, n2 in G[n1]:
        if weight + w < D[n2]:
            D[n2] = weight + w
            heapq.heappush(Q, (D[n2], n2))

for i in range(1, V+1):
    if D[i] == INF:
        print('INF')
    else:
        print(D[i])
