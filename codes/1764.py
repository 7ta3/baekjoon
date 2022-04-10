import sys

def binary_search (arr, value):
    start, end = 0, len(arr)-1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == value:
            return True
        if arr[mid] > value:
            end = mid - 1
        else :
            start = mid + 1
    return False

N, M = map(int, sys.stdin.readline().split())
N_list, M_list = [], []
for _ in range(N):
    N_list.append(sys.stdin.readline().strip())
N_list.sort()
for _ in range(M):
    M_list.append(sys.stdin.readline().strip())
M_list.sort()

ans = []
for i in N_list:
    if binary_search(M_list, i):
        ans.append(i)

print(len(ans))
for i in ans : print(i)