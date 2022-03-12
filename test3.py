import pprint
from collections import deque
import copy
# width =2
# height = 2
# diagonals = [[1,1],[2,2]]
# # 12
width = 51
height = 37
diagonals = [[17,19]]
#3225685

def solution(width, height, diagonals):
    G = [[[] for _ in range(width+1)] for _ in range(height+1)]
    for i in diagonals:
        G[width-i[1]][i[0]-1].append([i[0], width-i[1]+1, 1.214])
        G[width-i[1]+1][i[0]].append([i[0]-1, width-i[1], 1.214])
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    for i in range(width+1):
        for j in range(height+1):
            for d in range(4):
                nx = i + dx[d]
                ny = j + dy[d]
                if -1 < nx < width + 1 and -1 < ny < height + 1:
                    G[j][i].append([nx, ny, 1])
    # [x좌표, y좌표, 해당 노드에 가는데 필요한 거리]
    visited = [[False] * (width+1) for _ in range(height+1)]
    visited[height][0] = True
    S = [0, height, 0, visited, False]
    E = [width, 0]
    ST = deque([S])
    min_val = (width+1) * (height+1)
    while ST:
        x, y, distance, visited, visited_diagonal = ST.popleft()
        if [x, y] == E:
            if distance < min_val and visited_diagonal:
                answer, min_val = 1, distance
            elif distance == min_val and visited_diagonal:
                answer = (answer + 1) % 10000019

        for i in G[y][x]:
            if not visited[i[1]][i[0]]:
                if i[-1] == 1 :
                    temp_visited = copy.deepcopy(visited)
                    temp_visited[i[1]][i[0]] = True
                    ST.append([i[0], i[1], distance + i[-1], temp_visited, visited_diagonal])
                elif not visited_diagonal and i[-1] != 1:
                    temp_visited = copy.deepcopy(visited)
                    temp_visited[i[1]][i[0]] = True
                    ST.append([i[0], i[1], distance + i[-1], temp_visited, True])
    print(answer)
    return answer
solution(width, height, diagonals)