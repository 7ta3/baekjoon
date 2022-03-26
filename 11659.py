import sys
N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, input().split()))
sum_lst = [0] * (N+1)
for i in range(1, N+1):
    if i == 1:
        sum_lst[i] = lst[0]
    else:
        sum_lst[i] = sum_lst[i-1] + lst[i-1]

for _ in range(M):
    i, j = map(int, sys.stdin.readline().split())
    print(sum_lst[j] - sum_lst[i-1])