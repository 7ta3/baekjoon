from collections import deque
import sys
input = sys.stdin.readline
N = int(input())
P = [0] * (N + 1)
G = [[] for _ in range(N+1)]
for _ in range(N-1):
    A, B = map(int, input().split())
    G[A].append(B)
    G[B].append(A)

ST = deque([1])
while ST:
    s = ST.popleft()
    for i in G[s]:
        if not P[i]:
            P[i] = s
            ST.append(i)
for i in range(2, N+1):
    print(P[i])