n = 6
clockwise = False
def solution(n, clockwise):
    answer = [[0] * n for _ in range(n)]
    if clockwise == True:
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]
        points = [[0,0], [n-1,0], [n-1,n-1], [0,n-1]]
    else :
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        points = [[0,0], [0,n-1], [n-1,n-1], [n-1,0]]
    points_directions = [0, 1, 2, 3]
    points_cnt = [1, 1, 1, 1]
    break_point = [True, True, True, True]
    cnt_zero = n*n
    while cnt_zero > 0:
        for i in range(4):
            d = points_directions[i]
            x = points[i][0]
            y = points[i][1]
            cnt = points_cnt[i]

            answer[y][x] = cnt
            cnt_zero -= 1
            nx = x + dx[d]
            ny = y + dy[d]
            if -1 < nx < n and -1 < ny < n and answer[ny][nx] == 0:
                points[i][0], points[i][1] = nx, ny
                points_cnt[i] += 1
            else:
                d = (d+1) % 4
                nx = x + dx[d]
                ny = y + dy[d]
                if -1 < nx < n and -1 < ny < n and answer[ny][nx] == 0:
                    points_directions[i] = d
                    points[i][0], points[i][1] = nx, ny
                    points_cnt[i] += 1
                else:
                    break_point[i] = False
    return answer
solution(n,clockwise)