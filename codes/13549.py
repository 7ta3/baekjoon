from heapq import *
import sys
INF = sys.maxsize
input = sys.stdin.readline
N, K = map(int, input().split())
M = 100000

V = [INF] * (M + 1)
P = [0] * (M + 1)
V[N] = 0
Q = [(0, N)]
while Q:
    c, n = heappop(Q)
    for i in [ n - 1, n + 1, 2 * n]:
        if 0 <= i <= M and c + 1 < V[i]:
            V[i] = c + 1
            P[i] = n
            heappush(Q, (c + 1, i))

ans = [K]
temp = K
while True:
    if temp == N:
        break
    ans.append(P[temp])
    temp = P[temp]

print(V[K])
ans.reverse()
print(*ans)