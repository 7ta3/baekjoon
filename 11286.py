from heapq import *
import sys
input = sys.stdin.readline
N = int(input())
H = []
for _ in range(N):
    x = int(input())
    if x == 0:
        if not H:
            print(0)
        else:
            print(heappop(H)[1])
    else:
        heappush(H, (abs(x), x))
