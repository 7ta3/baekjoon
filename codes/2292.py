import math
N = int(input())
cnt = 0
N = math.ceil((N-1)/6)
while N > 0 :
    N -= (cnt+1)
    cnt+=1
print(cnt+1)
