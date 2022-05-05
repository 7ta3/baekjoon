from itertools import combinations

N, M, K = map(int, input().split())
L = [i for i in range(N)]
A = list(combinations(L, M))
B = list(combinations(L, M))

case = 0
for a in A:
    for b in B:
        cnt = 0
        flag = True
        for aa in a:
            for bb in b:
                if aa == bb and flag:
                    cnt += 1
                    if K <= cnt:
                        case += 1
                        flag = False
print(case / len(A) ** 2)