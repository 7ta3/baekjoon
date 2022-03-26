from collections import deque
N, M = map(int, input().split())
G = [[] for _ in range(N+1)]
for _ in range(M):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

cnt = 10**9
num = -1
for i in range(1, N+1):
    V = [0] * (N+1)
    ST = deque([i])
    while ST:
        s = ST.popleft()
        for j in G[s]:
            if not V[j] and j != i:
                ST.append(j)
                V[j] = V[s] + 1
    if sum(V) < cnt :
        cnt = sum(V)
        num = i
print(num)