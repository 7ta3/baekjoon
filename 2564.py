W, H = map(int,input().split())
N = int(input())
stores = []
for i in range(N):
    stores.append(list(map(int, input().split())))
DG = list(map(int, input().split()))
ans = 0
for i in stores:
    if DG[0] == 1:
        if i[0] == 1:
            ans += abs(DG[1]-i[1])
        elif i[0] == 2:
            ans += min(H + DG[1]+ i[1], H + (2*W - DG[1] - i[1]))
        elif i[0] == 3:
            ans += DG[1] + i[1]
        elif i [0] == 4:
            ans += W - DG[1] + i[1]
    elif DG[0] == 2:
        if i[0] == 1:
            ans += min(H + DG[1]+ i[1], H + (2*W - DG[1] - i[1]))
        elif i[0] == 2:
            ans += abs(DG[1]-i[1])
        elif i[0] == 3:
            ans += DG[1] + H - i[1]
        elif i [0] == 4:
            ans += W - DG[1] + H - i[1]
    elif DG[0] == 3:
        if i[0] == 1:
            ans += DG[1] + i[1]
        elif i[0] == 2:
            ans += H - DG[1] + i[1]
        elif i[0] == 3:
            ans += abs(DG[1]-i[1])
        elif i [0] == 4:
            ans += min(W + DG[1]+ i[1], W + (2*H - DG[1] - i[1]))
    elif DG[0] == 4:
        if i[0] == 1:
            ans += DG[1] + W - i[1]
        elif i[0] == 2:
            ans += W - DG[1] + H - i[1]
        elif i[0] == 3:
            ans += min(W + DG[1]+ i[1], W + (2*H - DG[1] - i[1]))
        elif i [0] == 4:
            ans += abs(DG[1]-i[1])
print(ans)