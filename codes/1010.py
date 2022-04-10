T = int(input())

for _ in range(T) :
    N, M = list(map(int, input().split()))
    max_val = max(N,M); min_val = min(N,M)
    dp_list = [[ 0 for i in range(max_val+1)] for i in range(max_val+1)]
    for i in range(0, max_val+1):
        for j in range(0, min_val+1):
            if i == j or j == 0 :
                dp_list[i][j] = 1
            elif j == 1 :
                dp_list[i][j] = i
            else:
                dp_list[i][j] = dp_list[i-1][j-1] + dp_list[i-1][j]
    print(dp_list[max_val][min_val])
