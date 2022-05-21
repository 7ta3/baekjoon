R, C, N = map(int, input().rsplit())
G = []
for _ in range(R):
    G.append(list(input()))

D = [(-1, 0), (1, 0), (0, 1), (0, -1)]

if N % 2 == 0:
    for _ in range(R):
        print('O' * C)

else:
    for i in range((N-1) // 2):
        temp = [['O'] * C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                if G[r][c] == 'O':
                    temp[r][c] = '.'
                    for d in D:
                        nr, nc = r + d[0], c + d[1]
                        if -1 < nr < R and -1 < nc < C:
                            temp[nr][nc] = '.'
        G = temp
    for i in G:
        print(''.join(i))

