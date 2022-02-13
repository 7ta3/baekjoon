from bisect import bisect_left, bisect_right
N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

N_list.sort()

def count_by_range(arr, left_val, right_val):
    right_idx = bisect_right(arr, right_val)
    left_idx = bisect_left(arr, left_val)
    return right_idx - left_idx

for i in M_list:
    cnt = count_by_range(N_list, i, i)
    print(cnt, end=" ")
