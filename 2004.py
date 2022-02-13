import sys
N, M = map(int,sys.stdin.readline().split())

num_2 = 0; num_5 = 0

def cnt(A, num):
    c = 0
    while A != 0:
        A //= num
        c += A
    return c

print(min(cnt(N,2) - cnt(N-M,2) - cnt(M,2), cnt(N,5) - cnt(N-M,5) - cnt(M,5)))
