N, S, M = map(int, input().split())
A = list(map(int, input().split()))

DP = [set() for _ in range(N)]
for i in range(N):
    if i == 0:
        if S + A[i] <= M:
            DP[i].add(S + A[i])
        if 0 <= S - A[i]:
            DP[i].add(S - A[i])
    else:
        for j in DP[i-1]:
            if j + A[i] <= M:
                DP[i].add(j + A[i])
            if 0 <= j - A[i]:
                DP[i].add(j - A[i])
    if not DP[i]:
        print(-1)
        exit(0)
print(max(DP[-1]))
