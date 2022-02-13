import sys

N = int(sys.stdin.readline())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline().strip()))
nums.sort()
cnt_p = [0] * 4001
cnt_m = [0] * 4001

for i in range(N):
    if nums[i] < 0 :
        cnt_m[-nums[i]] += 1
    else :
        cnt_p[nums[i]] += 1

r1 = round(sum(nums) / N)
r2 = nums[int((N+1)/2) - 1]

max_val = 0
max_lst = []

for i in range(4001):
    if max_val < cnt_p[i] :
        max_val = cnt_p[i]
        max_lst =[i]
    elif max_val == cnt_p[i]:
        max_lst.append(i)
    if max_val < cnt_m[i] :
        max_val = cnt_m[i]
        max_lst =[-i]
    elif max_val == cnt_m[i]:
        max_lst.insert(0,-i)

if len(max_lst) > 1 :
    r3 = max_lst[1]
else :
    r3 = max_lst[0]    

r4 = nums[-1] - nums[0]

print(r1)
print(r2)
print(r3)
print(r4)