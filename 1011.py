import sys
import math

T = int(input())
for _ in range(T):
    A, B = list(map(int, sys.stdin.readline().split()))

    distance = B - A
    max = int(math.sqrt(distance))

    if distance == max ** 2 :
        cnt = 2 * max - 1

    elif max ** 2 < distance <= max ** 2 + max:
        cnt = 2 * max
    else :
        cnt = 2 * max + 1
    print(cnt)