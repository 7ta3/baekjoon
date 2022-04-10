from collections import deque
import sys
N = int(sys.stdin.readline())
lst = deque()

for _ in range(N):
    a = list(sys.stdin.readline().split())
    if a[0] == 'push_front':
        lst.appendleft(int(a[1]))
    elif a[0] == 'push_back':
        lst.append(int(a[1]))
    elif a[0] == 'pop_front':
        if len(lst) == 0 : print(-1)
        else : print(lst.popleft())
    elif a[0] == 'pop_back':
        if len(lst) == 0 : print(-1)
        else : print(lst.pop())
    elif a[0] == 'size':
        print(len(lst))
    elif a[0] == 'empty':
        if len(lst) == 0 : print(1)
        else : print(0)
    elif a[0] == 'front':
        if len(lst) == 0 : print(-1)
        else : print(lst[0])
    elif a[0] == 'back':
        if len(lst) == 0 : print(-1)
        else : print(lst[-1])
