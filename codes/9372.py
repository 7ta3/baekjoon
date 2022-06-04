import sys
input = sys.stdin.readline

def dfs(n1):
    V[n1] = True
    D[n1] = 1
    for n2 in G[n1]:
        if not V[n2]:
            dfs(n2)
            D[n1] += D[n2]

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    G = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        G[a].append(b)
        G[b].append(a)

    V = [False] * (N+1)
    D = [0] * (N+1)
    dfs(1)
    print(D[1]-1)