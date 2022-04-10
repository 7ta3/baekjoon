import heapq, sys
T = int(sys.stdin.readline())

for t in range(1, T+1):
    H = []
    L = []
    V = [False] * 1000000
    k = int(sys.stdin.readline())
    for i in range(k):
        a = list(sys.stdin.readline().split())
        if a[0] == 'I':
            heapq.heappush(L, (int(a[1]), i))
            heapq.heappush(H, (-int(a[1]), int(a[1]), i))
            V[i] = True

        elif a[0] == 'D' and a[1] == '1':
            while H and not V[H[0][-1]]:
                heapq.heappop(H)
            if H:
                V[H[0][-1]] = False
                heapq.heappop(H)

        elif a[0] == 'D' and a[1] == '-1':
            while L and not V[L[0][-1]]:
                heapq.heappop(L)
            if L:
                V[L[0][-1]] = False
                heapq.heappop(L)

    while H and not V[H[0][-1]]:
        heapq.heappop(H)

    while L and not V[L[0][-1]]:
        heapq.heappop(L)

    if not L:
        print('EMPTY')
    else:
        print(heapq.heappop(H)[1], heapq.heappop(L)[0])

