N = int(input())
nums = list(map(int,input().split()))
if N == 1:
    print(nums[0] ** 2)
else :
    print(min(nums) * max(nums))