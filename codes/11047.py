import sys
N, K = list(map(int,input().split()))
coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline().strip()))

cnt = 0

for i in coins[::-1]:
    if K // i > 0:
        cnt += (K // i)
        K %= i
    if K == 0 :
        break
print(cnt)