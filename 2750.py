import sys

N = int(input())
lst = []

for _ in range(N) :
    x = int(input())
    lst.append(x)

lst.sort()
for i in lst : print(i)