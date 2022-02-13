import math, sys

T = int(sys.stdin.readline().strip())

# def partition_func(N):
#   if N < 2:
#     return 1
#   else :
#     return partition_func(N-2) + partition_func(math.floor(N/2))
    
# for _ in range(T):
#   a = int(sys.stdin.readline().strip())
#   print(partition_func(a))

dp_list = [1] * 1001
for i in range(1,1001):
  for j in range(0,i+1):
    if (i-j) % 2 == 0 and (i-j > 0):
      dp_list[i] += dp_list[(i-j)//2]

for _ in range(T):
  a = int(sys.stdin.readline().strip())
  print(dp_list[a])