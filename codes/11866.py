from collections import deque

N, K = map(int, input().split())
lst = deque()
lst = deque([str(i) for i in range(1, N+1)])
dead = []
while len(lst) != 0:
    for i in range(K-1):
        a = lst.popleft()
        lst.append(a)
    dead.append(lst.popleft())

print('<', end='')
print(', '.join(dead), end='')
print('>', end='')