import sys
N = int(sys.stdin.readline())
mems = []
for _ in range(N):
    m = list(map(str, sys.stdin.readline().split()))
    mems.append(m)

mems.sort(key= lambda a: int(a[0]))
for i in mems:
    print(i[0], i[1])