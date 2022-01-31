from re import L
import sys
N = int(input())
x = [int(i) for i in sys.stdin.readline().split()]
cnt = 0
for i in x :
    cnt = cnt + 1 if (i == 1) else cnt
    for j in range(2, i):
        if (i % j == 0) :
            cnt += 1
            break
print(N - cnt)