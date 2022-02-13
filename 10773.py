import sys
K = int(input())

lst = []
for _ in range(K):
    a = int(sys.stdin.readline())
    if a == 0 : lst.pop()
    else : lst.append(a)
print(sum(lst))