N, M = list(map(int,input().split()))
input_list = []

x = N - 8 + 1
y = M - 8 + 1

cases = ['W', 'B']
cnt = N * M

for _ in range(N):
    input_list.append(input())

for k in range(2):
    for d_x in range(x):
        for d_y in range(y):
            cn = k
            cnt_d = 0
            for i in range(8):
                for j in range(8):
                    if input_list[i+d_x][j+d_y] != cases[cn] :
                        cnt_d += 1
                    cn = not(cn)
                cn = not(cn)
            if cnt > cnt_d :
                cnt = cnt_d
print(cnt)