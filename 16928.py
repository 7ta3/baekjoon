N , M = map(int, input().split())
visited = [False] * 101
lst = []
for i in range(N+M):
    lst.append(list(map(int, input().split())))

ST = [[1, 0]]
visited[1] = True
E = 100
cnt = 0
while ST:
    s = ST.pop(0)
    for i in lst:
        if i[0] == s[0]:
            s = [i[1], s[1]]
            break
    if s[0] == 100:
        break
    for i in range(1, 7):
        ns = s[0] + i
        if ns <= 100 and not visited[ns]:
            ST.append([ns, s[1]+1])
            visited[ns] = True
print(s[1])

