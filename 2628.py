W, H = map(int, input().split())
N = int(input())
lst_W = []; lst_H = []

for _ in range(N):
    a = list(map(int, input().split()))
    if a[0] == 0 : lst_W.append(a[1]) # 가로로 자르므로 세로 길이 영향
    else: lst_H.append(a[1]) # 세로로 자르므로 가로 길이에 영향

max_W = W; max_H = H
if lst_H != []: # 가로 길이
    lst_H.sort()
    L_H = len(lst_H)
    max_W = lst_H[0]
    for i in range(1, L_H):
        max_W = max(max_W, lst_H[i] - lst_H[i-1])
    max_W = max(max_W, W - lst_H[-1])

if lst_W != []: # 세로 길이
    lst_W.sort()
    L_W = len(lst_W)
    max_H = lst_W[0]
    for i in range(1, L_W):
        max_H = max(max_H, lst_W[i] - lst_W[i-1])
    max_H = max(max_H, H - lst_W[-1])
print(max_H * max_W)