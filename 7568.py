import sys

N = int(input())
members = []
ranking = [1] * N
for _ in range(N):
    members.append(list(map(int,sys.stdin.readline().split())))
print(members)

for idx, i in enumerate(members):
    for j in members:
        if i[0] < j[0] and i[1] < j[1]:
            ranking[idx] += 1
for i in ranking:
    print(i, end=" ")