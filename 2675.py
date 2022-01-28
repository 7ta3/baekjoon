import sys
T = int(input())
for i in range(T) :
    s = ''
    a, b = map(str, sys.stdin.readline().split())
    for j in b:
        s += j*int(a)
    print(s)