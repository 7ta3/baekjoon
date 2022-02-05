import sys
a = list(map(int, sys.stdin.readline().split()))

while a[0] != 0 and a[1] != 0 and a[2] != 0 :
    max_a = a.pop(a.index(max(a)))
    if max_a**2 == (a[0]**2 + a[1]**2) :
        print('right')
    else :
        print('wrong')
    a = list(map(int, sys.stdin.readline().split()))