N, M, R = map(int, input().split())
arr = []
result = [['S' for _ in range(M)] for _ in range(N)]
for _ in range(N):
    arr.append(list(map(int, input().split())))

d = {'E':[1,0], 'W':[-1,0], 'S':[0,1], 'N':[0,-1]}
cnt = 0
for _ in range(R):
    Y, X, D = input().split()
    X = int(X) - 1
    Y = int(Y) - 1
    B, A = map(int, input().split())
    B -= 1
    A -= 1

    t = arr[Y][X]
    if result[Y][X] == 'F':
        result[B][A] = 'S'
        continue
    while -1 < X < M and -1 < Y < N and t > 0:
        if result[Y][X] == 'S':
            result[Y][X] = 'F'
            cnt += 1
            t = max(t, arr[Y][X])

        X += d[D][0]
        Y += d[D][1]
        t -= 1
    result[B][A] = 'S'
    # 수비를 하면 거기 전까지만 넘어진다는 거 아니었냐... 진짜 너무하네 하나 세울 거면 수비를 왜해
print(cnt)
for i in result:
    print(*i)
