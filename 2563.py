rg = [[0 for i in range(101)] for i in range(101)]
N = int(input())
for _ in range(N):
    blk = list(map(int, input().split()))
    for i in range(blk[0], blk[0]+10):
        for j in range(blk[1], blk[1]+10):
            rg[i][j] = 1
ans = 0
for i in range(1,101):
    ans += sum(rg[i])
print(ans)