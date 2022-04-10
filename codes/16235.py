N, M, K = map(int, input().split())
A = []
for _ in range(N):
    A.append(list(map(int, input().split())))
# 로봇 양분
T = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    y, x, age = map(int, input().split())
    T[y-1][x-1].append(age)
# 나무 나이
F = [[5] * N for _ in range(N)]
# 땅의 양분
D = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
for _ in range(K):
    for i in range(N):
        for j in range(N):
            temp = []
            if T[j][i]:
                T[j][i].sort()
                for k in range(len(T[j][i])):
                    if F[j][i] >= T[j][i][k]:
                        F[j][i] -= T[j][i][k]
                        T[j][i][k] += 1
                    else:
                        temp = T[j][i][k:]
                        T[j][i] = T[j][i][:k]
                        break
            for k in temp:
                F[j][i] += k // 2
    # 봄 / 여름
    for i in range(N):
        for j in range(N):
            if T[j][i]:
                for k in T[j][i]:
                    if not (k % 5):
                        for d in D:
                            nx = i + d[0]
                            ny = j - d[1]
                            if - 1 < nx < N and -1 < ny < N:
                                T[ny][nx].append(1)
    # 가을
    for i in range(N):
        for j in range(N):
            F[j][i] += A[j][i]
    # 겨울
cnt = 0
for i in range(N):
    for j in range(N):
        if T[j][i]:
            cnt += len(T[j][i])
print(cnt)



