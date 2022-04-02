import sys

T = int(sys.stdin.readline())

for _ in range(T):
    M, N, x, y = map(int, sys.stdin.readline().split())

    if x <= M and y <= N:
        a, b = x, (x % N)
        if b == 0:
            b = N
    else:
        print(-1)
        continue

    cnt = x
    start_b = b
    while True:
        if b == y:
            print(cnt)
            break
        if cnt > (M*N+1):
            print(-1)
            break
        cnt += M
        b = (cnt % N)
        if b == 0:
            b = N