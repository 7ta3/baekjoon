import sys
from collections import deque, defaultdict

N, Q = map(int, sys.stdin.readline().split())
USADO = defaultdict(list)
for _ in range(N-1):
    p, q, r = map(int, sys.stdin.readline().split())
    USADO[p].append([q, r])
    USADO[q].append([p, r])

for _ in range(Q):
    K, A = map(int, sys.stdin.readline().split())
    V = [False] * (N + 1)
    V[A] = True
    ST = deque([])
    cnt = 0
    for j in USADO[A]:
        V[j[0]] = True
        ST.append(j)

    while ST:
        s = ST.popleft()
        if s[1] >= K:
            if s[0] != A and s[1] >= K:
                cnt += 1
        for j in USADO[s[0]]:
            if not V[j[0]]:
                ST.append([j[0], min(s[1], j[1])])
                V[j[0]] = True
    print(cnt)
