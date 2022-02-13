import sys
N = int(input())
lst = []
for _ in range(N):
    a = list(sys.stdin.readline().split())
    if a[0] == 'push': lst.append(int(a[1]))
    elif a[0] == 'pop':
        if lst == []: print(-1)
        else : p = lst[-1] ; lst = lst[:-1]; print(p)
    elif a[0] == 'size': print(len(lst))
    elif a[0] == 'empty':
        if lst == [] : print(1)
        else : print(0)
    elif a[0] == 'top' : 
        if lst == [] : print(-1)
        else : print(lst[-1])