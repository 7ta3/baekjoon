import sys
M = int(sys.stdin.readline())
S = [0]*21
for i in range(M):
    a = list(sys.stdin.readline().split())
    if len(a) > 1 : a[1] = int(a[1])
    if a[0] == 'add': S[a[1]] = 1
    elif a[0] == 'remove': S[a[1]] = 0
    elif a[0] == 'check':
        if S[a[1]] == 1: print(1)
        else: print(0)
    elif a[0] == 'toggle':
        if S[a[1]] == 1: S[a[1]] = 0
        else: S[a[1]] = 1
    elif a[0] == 'all':
        S = [1] * 21
    elif a[0] == 'empty':
        S = [0] * 21

