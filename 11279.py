import heapq, sys

N = int(sys.stdin.readline().strip())
heap = []
for _ in range(N):
    a = int(sys.stdin.readline().strip())
    if heap and a == 0:
        print(heapq.heappop(heap)[1])

    elif not heap and a == 0:
        print(0)
    else:
        heapq.heappush(heap, (-a, a))
