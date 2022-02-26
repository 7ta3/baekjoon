import pprint
A = input()
B = input()
max_len = max(len(A),len(B))
dp = [[''] * len(B) for _ in range((len(A)))]
ans = ''

chk = False
for i in range(len(A)):
    if A[i] == B[0] or chk :
        dp[i][0] = B[0]
        chk = True
        ans = B[0]

chk = False
for i in range(len(B)):
    if B[i] == A[0] or chk :
        dp[0][i] = A[0]
        chk = True

for i in range(1, len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:
            dp[i][j] = dp[i-1][j-1] + A[i]
            if len(ans) < len(dp[i][j]): ans = dp[i][j]
        else:
            if len(dp[i-1][j]) > len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]
pprint.pprint(dp)
