import sys
from math import sqrt
from math import gcd
N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline()))
lst.sort()
arr = []
for i in range(N-1):
    arr.append(lst[i+1]-lst[i])

d = arr[0]
for i in arr[1:]:
    A , B = max(i, d), min(i, d)
    while A % B != 0:
        A, B = B, A % B
    m = B
    if d > m : d = m

ans = [d]
for i in range(2,int(sqrt(d))+1):
    if d % i == 0:
        ans.append(i)
        ans.append(d//i)

ans = list(set(ans))
ans.sort()
for i in ans : print(i, end=" ")