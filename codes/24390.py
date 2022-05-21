from heapq import *
M1, M2, _, S1, S2 = list(input())
M = int(M1 + M2)
S = int(S1 + S2)
T = 60 * M + S

cnt = 0
cnt += (T // 600)
T %= 600
cnt += (T // 60)
T %= 60
Q = [(cnt, 0, False)]
while Q:
    c, t, p = heappop(Q)

    if t == T and p:
        print(c)
        break

    for i in [10, 60, 600]:
        if i + t <= T:
            heappush(Q, (c+1, i+t, p))
    if p:
        if t + 30 <= T:
            heappush(Q, (c+1, 30+t, p))
    else:
        if t + 30 <= T:
            heappush(Q, (c+1, t + 30, True))
        heappush(Q, (c+1, t, True))
