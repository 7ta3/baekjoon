from collections import deque

N, L, R = map(int, input().split())
countries = []
for _ in range(N):
    countries.append(list(map(int, input().split())))

visited = [[False] * N for _ in range(N)]
D = [(1,0), (-1,0), (0,1), (0,-1)]
t = 0 # 며칠동안 인구 이동이 일어날지
while True: # 인구 이동
    visited = [[False] * N for _ in range(N)]
    union = [] # 전체 연합
    union_info = [] # 각 연합의 정보 (연합을 이루고 있는 칸의 개수, 연합의 인구수)
    for x in range(N):
        for y in range(N):
            if not visited[y][x]:
                ST = deque([[x, y, countries[y][x]]])
                visited[y][x] = True
                temp_union = [] # 하나의 연합
                temp_union_info = [0, 0] # 연합을 이루고 있는 칸의 개수, 연합의 인구수
                while ST:
                    s = ST.popleft()
                    temp_union.append(s)
                    temp_union_info = [temp_union_info[0]+1, temp_union_info[1]+countries[s[1]][s[0]]]
                    for d in D:
                        nx = s[0] + d[0]
                        ny = s[1] + d[1]
                        if - 1 < nx < N and -1 < ny < N and not visited[ny][nx]:
                            if L <= abs(s[-1] - countries[ny][nx]) <= R: # 인구 수에 따라서 연합을 할지 말지
                                ST.append([nx, ny, countries[ny][nx]])
                                visited[ny][nx] = True
                if len(temp_union) > 1: # 연합이 생긴 경우 union에 추가
                    union.append(temp_union)
                    union_info.append(temp_union_info)
    if not union:
        break
    t += 1
    for i in range(len(union)):
        p = union_info[i][1] // union_info[i][0] # 편의상 소수점은 버린다
        for x, y, _ in union[i]:
            countries[y][x] = p
print(t)