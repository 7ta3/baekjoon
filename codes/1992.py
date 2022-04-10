def Quad_Tree(arr, N):
    global ans
    a = arr[0][0]
    for i in range(N):
        for j in range(N):
            if arr[j][i] != a:
                N //= 2
                ans += '('
                for y in range(2):
                    for x in range(2):
                        temp = []
                        for k in range(N):
                            temp.append(arr[N*y+k][N*x:N*(x+1)])
                        Quad_Tree(temp, N)
                ans += ')'
                return
    ans += a
N = int(input())
G = []
for _ in range(N):
    G.append(list(input()))
ans = ''
Quad_Tree(G, N)
print(ans)
