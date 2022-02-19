import sys
N = int(sys.stdin.readline().strip())
lst = list(map(int, sys.stdin.readline().split()))
cnt = 1; ans = 0
for i in range(N-1):
    if lst[i] <= lst[i+1]:
        cnt+=1
    else :
        ans = max(cnt, ans)
        cnt = 1
ans = max(cnt, ans)

cnt = 1
for i in range(N-1):
    if lst[i+1] <= lst[i]:
        cnt += 1
    else :
        ans = max(cnt, ans)
        cnt = 1
ans = max(cnt, ans)
print(ans)