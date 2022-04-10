from itertools import permutations
N, M = map(int, input().split())
A = list(map(int, input().split()))
temp = sorted(list(set(permutations(A, M))))
for i in temp:
    print(*i)