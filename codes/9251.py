A = input()
B = input()
L_A = len(A)
L_B = len(B)
dp = [[0 for _ in range(L_B)] for _ in range(L_A)]

chk = False
for i in range(L_A):
    if A[i] == B[0] or chk:
        dp[i][0] = 1
        chk = True

chk = False
for i in range(L_B):
    if B[i] == A[0] or chk:
        dp[0][i] = 1
        chk = True

for i in range(1, L_A):
    for j in range(1, L_B):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
print(dp[-1][-1])

