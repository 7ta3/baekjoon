import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
A = sorted(list(map(int, input().split())))
AA = [0] * (N+1)
AA[1] = A[0]
for i in range(2, N+1):
    AA[i] = AA[i-1] + A[i-1]
for _ in range(Q):
    L, R = map(int, input().split())
    print(AA[R]-AA[L-1])
