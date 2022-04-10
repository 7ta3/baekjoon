N, K = list(map(int, input().split()))
dp_list = [[0 for _ in range(1001)] for _ in range(1001)]

for i in range(1, N+1):
    for j in range(0, K+1):
        if j == 0 or i == j :
            dp_list[i][j] = 1
        elif j == 1 :
            dp_list[i][j] = i
        else:
            dp_list[i][j] = dp_list[i-1][j-1] + dp_list[i-1][j]

print(dp_list[N][K] % 10007)
