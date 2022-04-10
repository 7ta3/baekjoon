N = int(input())

def dragon_curve(x, y): # arr를 뒤집고 각각의 방향에서 90도 회전하여 앞에서부터 순차적으로 그려보면 다음 세대 드래곤 커브
    for i in arr[::-1]:
        x += D[(i+1) % 4][0]
        y += D[(i+1) % 4][1]
        if -1 < x < 101 and -1 < y < 101:
            lst.append((x,y))
        arr.append((i+1) % 4)
    return x, y

def cnt_square(x, y): # 방문한 좌표들로 그려지는 사각형의 수
    global cnt
    square = [(0,1), (1,0), (1,1)]
    temp = 0
    for i in square:
        nx = x + i[0]
        ny = y + i[1]
        if (nx, ny) in lst:
            temp += 1
    if temp == 3:
        cnt += 1

D = [(1,0), (0,-1), (-1,0), (0,1)] # 우,상,좌,하 : 0, 1, 2, 3
lst = [] # 방문한 좌표

for _ in range(N):
    x, y, d, g = map(int, input().split())
    arr = [d]
    lst.append((x, y))
    x += D[d][0]
    y += D[d][1]
    if -1 < x < 101 and -1 < y < 101:
        lst.append((x, y))
    # 초기화

    for i in range(g):
        x, y = dragon_curve(x, y)
lst = set(lst) # 중복 제거
lst = list(lst)

cnt = 0
for x, y in lst:
    cnt_square(x, y)
print(cnt)