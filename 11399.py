N = int(input())

lst = [int(i) for i in input().split()]

lst.sort()
t_sum = 0

for i in range(N):
    t_sum += lst[i] * (N-i) 

print(t_sum)