import math
M, N = list(map(int, input().split()))

rt = int(math.sqrt(N))
lst = [True] * (N + 1)
for i in range(2, rt + 1):
    if lst[i] == True:
        for j in range(2 * i, N + 1, i):
            lst[j] = False
for i in range(M, N+1):
    if i == 1:
        continue
    if lst[i] == True: print(i)
# 에라토스테네스의 체