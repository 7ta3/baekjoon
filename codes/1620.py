import sys
N, M = map(int, sys.stdin.readline().split())
dic = {}
for i in range(1, N+1):
    a = input()
    dic[str(i)] = a
    dic[a] = str(i)

for i in range(M):
    print(dic[sys.stdin.readline().strip()])