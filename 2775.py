T = int(input())

for _ in range(T):
    k = int(input())
    n = int(input())
    under = [i for i in range(1, n + 1)]
    present = list(under)
    for i in range(1, k+1):
        for j in range(n):
            present[j] = sum(under[:j+1])
        under = list(present)
    print(present[-1])