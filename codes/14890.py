N, L = map(int, input().split())
G = []
def path(arr):
    cnt, val = 0, arr[0]
    for i in range(1, N):
        if arr[i-1] == arr[i]:
            cnt += 1
            continue
        else:
            if arr[i-1] - arr[i] == -1 and cnt >= L:
                cnt, val = 0, arr[i]
            else:
                return False
    return True
ans = 0
for _ in range(N):
    l = list(map(int, input().split()))
    if path(l): print(l) ;ans += 1
    if path(l[::-1]): print(l) ;ans += 1
    G.append(l)

for i in range(N):
    l = []
    for j in range(N):
        l.append(G[j][i])
    print(l)
    if path(l): print('here', l);ans += 1
    if path(l): print('here', l);ans += 1
print(ans)
