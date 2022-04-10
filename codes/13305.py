N = int(input())
distance = list(map(int,input().split()))
oils = list(map(int,input().split()))

cost = 0
oil = [0, oils[0]]
for i in range(1, len(oils)-1):
    if oil[1] > oils[i]:
        for j in range(oil[0], i):
            cost += distance[j] * oil[1]
        oil=[i, oils[i]]
if len(distance) > oil[0]:
    for i in range(oil[0],len(distance)) : cost += distance[i] * oil[1]
print(cost)
