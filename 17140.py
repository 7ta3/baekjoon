r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

N , M = 3, 3
def extension(M, N):
    L = M
    temp_A = []
    for i in range(N):
        temp_arr = list(A[i])
        dic = {}
        for j in temp_arr:
            if j not in dic.keys() and j != 0:
                dic[j] = 1
            elif j != 0:
                dic[j] += 1
        a = list(dic.items())
        a.sort(key=lambda x: (x[1], x[0]))
        temp_a = []
        for key, val in a:
            temp_a.append(key)
            temp_a.append(val)
        L = max(len(temp_a), L)
        temp_A.append(temp_a)
    for i in temp_A:
        if len(i) < L:
            i.extend([0]*(L-len(i)))
    return temp_A, L

def transpose():
    temp_A = [[0]*N for _ in range(M)]
    for i in range(M):
        for j in range(N):
            temp_A[i][j] = A[j][i]
    return temp_A

def reverse_transpose():
    temp_A = [[0]*M for _ in range(N)]
    for i in range(M):
        for j in range(N):
            temp_A[j][i] = A[i][j]
    return temp_A

for i in range(101):
    if -1 < r-1 < N and -1 < c-1 < M and A[r-1][c-1] == k:
        print(i)
        break
    if N >= M :
        A, M = extension(M, N)
    else:
        A = transpose()
        A, N = extension(N, M)
        A = reverse_transpose()
else:
    print(-1)