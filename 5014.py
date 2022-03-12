from collections import deque
F, S, G, U, D = map(int, input().split())
visited = [False] * (F+1)
ST = deque([[S, 0]])
visited[S] = True
while ST:
    s = ST.popleft()
    if s[0] == G:
        break
    s_up = s[0] + U
    if s_up <= F and not visited[s_up]:
        ST.append([s_up, s[-1]+1])
        visited[s_up] = True
    s_down = s[0] - D
    if s_down > 0 and not visited[s_down]:
        ST.append([s_down, s[-1]+1])
        visited[s_down] = True
else:
    print('use the stairs')
    exit(0)
print(s[-1])
