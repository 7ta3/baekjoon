N = int(input())
G = []
for i in range(N):
    G.append(list(map(int, input().split())))

ans = [[0] * N for _ in range(N)]

def DFS(n, s, depth):
    if depth != 0:
        ans[s][n] = 1

    for i in range(N):
        if not V[i] and G[n][i]:
            V[i] = True
            DFS(i, s, depth + 1)

for i in range(N):
    V = [False] * N
    DFS(i, i, 0)

for i in range(N):
    print(*ans[i])


