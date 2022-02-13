import sys

N = int(sys.stdin.readline().strip())
Xs = list(map(int, sys.stdin.readline().split()))

dic = {}
Xs_set = sorted(list(set(Xs)))

for i in range(len(Xs_set)):
    dic[Xs_set[i]] = i

for i in Xs : print(dic[i], end = " ")
