from collections import deque
N, M, K, X = map(int, input().split())
G = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    G[A].append(B)

ans = []
ST = deque([X])
V = [0] * (N+1)
V[X] = 0
while ST:
    x = ST.popleft()
    for j in G[x]:
        if not V[j] and j != X:
            ST.append(j)
            V[j] = V[x] + 1

flag = False
for i in range(1, N+1):
    if V[i] == K:
        print(i)
        flag = True
if not flag:
    print(-1)