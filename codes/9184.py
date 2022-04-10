def dp(a,b,c):
    if a <= 0 or b <= 0 or c <= 0 :
        return 1
    elif a > 20 or b > 20 or c > 20:
        return dp(20, 20, 20)
    if dp_list[a][b][c] != 0 :
        return dp_list[a][b][c]
    if a < b and b < c :
        dp_list[a][b][c] = dp(a, b, c-1) + dp(a, b-1, c-1) - dp(a,b-1,c)
        return dp_list[a][b][c]
    else:
        dp_list[a][b][c] = dp(a-1, b, c) + dp(a-1,b-1,c) + dp(a-1,b,c-1) - dp(a-1, b-1,c-1)
        return dp_list[a][b][c]

a, b, c = map(int, input().split())
dp_list = [[[0 for _ in range(21)] for _ in range(21)] for _ in range(21)]

while a != -1 or b != -1 or c != -1 :
    print('w(%d, %d, %d) ='%(a,b,c), dp(a,b,c))
    a, b, c = map(int, input().split())