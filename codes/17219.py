import sys
N, M = map(int, sys.stdin.readline().split())
memo = {}
for _ in range(N):
    a, b = list(sys.stdin.readline().split())
    memo[a] = b
for _ in range(M):
    print(memo[sys.stdin.readline().strip()])