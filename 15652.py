from itertools import combinations_with_replacement
N, M = map(int, input().split())
A = [i for i in range(1, N+1)]
for i in combinations_with_replacement(A, M):
    print(*i)