T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = list(map(int,input().split()))
    distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    r_max = max(r1, r2)
    r_min = min(r1, r2)
    if distance == 0:
        if r1 == r2 :
            print(-1)
        else :
            print(0)
    elif distance == r_max - r_min :
        print(1)
    elif distance == r1 + r2 :
        print(1)
    elif distance > r_max + r_min :
        print(0)
    elif distance + r_min < r_max :
        print(0)
    elif distance < r_max + r_min :
        print(2)

# 아 ㅋㅋ 이거 이렇게 하는거 아닌데 엌ㅋㅋ
