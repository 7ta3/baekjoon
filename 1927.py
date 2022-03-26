import heapq, sys

N = int(sys.stdin.readline().strip())
heap = []
for i in range(N):
    a = int(sys.stdin.readline().strip())
    if heap and a == 0:
        print(heapq.heappop(heap))
    elif not heap and a == 0:
        print(0)
    else:
        heapq.heappush(heap, a)
