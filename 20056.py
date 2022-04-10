N, M, K = map(int, input().split())
D = [(0, N-1), (1, N-1), (1, 0), (1, 1), (0, 1), (N-1, 1), (N-1, 0), (N-1, N-1)]
A = []
for _ in range(M):
    l = list(map(int, input().split()))
    l[0] -= 1
    l[1] -= 1
    A.append(list(l))


for _ in range(K):
    if not A:
        break

    # 모든 파이어볼 이동
    for i in range(len(A)):
        r, c, m, s, d = A[i]
        nr = (r + D[d][1] * s) % N
        nc = (c + D[d][0] * s) % N
        A[i] = list([nr, nc, m, s, d])

    # 같은 칸에 있는 파이어볼은 모두 하나로 합쳐진다. (속력 질량 처리 / 방향 체크)
    A.sort(key=lambda x:(x[0], x[1]))
    flag, i, cnt = True, 1, 1 # flag: True == 방향이 모두 홀수이거나 짝수 / False == 그렇지 않은 경우
    while i < len(A):
        temp = A[i-1]
        x = A[i]
        if temp[0] == x[0] and temp[1] == x[1]:
            A[i - 1][2] += x[2]
            A[i - 1][3] += x[3]
            if (temp[-1] % 2) != (x[-1] % 2): # 그렇지 않으면
                flag = False
            cnt += 1
            A.pop(i)
        else:
            if cnt > 1:
                A[i-1][3] //= cnt
                A[i-1][2] //= 5
                if flag: A[i-1][-1] = -2
                else: A[i - 1][-1] = -1
            flag = True
            i += 1
            cnt = 1
    if cnt > 1:
        A[i-1][3] //= cnt
        A[i-1][2] //= 5
        if flag: A[i-1][-1] = -2
        else: A[i-1][-1] = -1

    # 파이어볼은 4개의 파이어볼로 나누어진다.
    i, L = 0, len(A)
    while i < L:
        x = list(A[i])
        if x[-1] < 0:
            if x[2] > 0:
                if x[-1] == -1: # flag == False
                    for d in range(8):
                        if d % 2:
                            x[-1] = d
                            A.append(list(x))
                elif x[-1] == -2: # flag == True
                    for d in range(8):
                        if not d % 2:
                            x[-1] = d
                            A.append(list(x))
            L -= 1
            A.pop(i)
        else:
            i += 1
ans = 0
for i in A:
    ans += i[2]
print(ans)