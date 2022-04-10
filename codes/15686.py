from itertools import combinations
import copy
N, M = map(int, input().split())
city = []
ck = [] # 치킨집
for i in range(N):
    a = list(map(int, input().split()))
    city.append(a)
    for j in range(N):
        if a[j] == 2:
            ck.append([j, i])

lst = list(combinations(ck, M)) # 살아남은 치킨집

D = [(1,0), (-1,0), (0,1), (0,-1)]
dis = 10 ** 10 # 살아남은 치킨집과 최소 거리
for i in lst:
    temp_city = copy.deepcopy(city)
    temp_dis = 0 # 해당 경우에서 살아남은 치킨집과 최소 거리
    for y in range(N):
        for x in range(N):
            if temp_city[y][x] == 1:
                temp = 10 ** 10 # 가까운 치킨집과 거리
                for a in i:
                    temp = min(temp, abs(a[0]-x)+abs(a[1]-y))
                temp_dis += temp
    dis = min(temp_dis, dis)
print(dis)






