from itertools import permutations
N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))
for i in permutations(A, M):
    print(*i)