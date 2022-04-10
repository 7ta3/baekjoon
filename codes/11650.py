import sys

N = int(input())
points = []
for _ in range(N) :
    p = list(map(int, sys.stdin.readline().split()))
    points.append(p)

points.sort(key = lambda a : a[1])
points.sort(key = lambda a : a[0])

for i in points :
    print(i[0],i[1])