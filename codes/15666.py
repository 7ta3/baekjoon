from itertools import combinations_with_replacement
N, M = map(int, input().split())
A = sorted(list(set(map(int, input().split()))))
for i in combinations_with_replacement(A,M):
    print(*i)