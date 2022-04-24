import sys
input = sys.stdin.readline
N = int(input())

DP = [0] * N
for i in range(N):
    if i == 0:
        DP[i] = 3
    elif i == 1:
        DP[i] = 7
    else:
        DP[i] = DP[i-1] * 2 + DP[i-2]
print(DP[-1])