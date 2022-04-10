import sys
input = sys.stdin.readline

N = int(input())
A = [0] + list(map(int, input().split()))
DP = [0] * (N+1)
temp = [-float('inf')]


def find(e):
    start = 0
    end = len(temp) - 1
    while start <= end:
        mid = (start + end) // 2
        if temp[mid] == e:
            return mid
        elif temp[mid] < e:
            start = mid + 1
        else:
            end = mid - 1
    return start

for i in range(1, N+1):
    if temp[-1] < A[i]:
        temp.append(A[i])
        DP[i] = len(temp) - 1
    else:
        idx = find(A[i])
        DP[i] = idx
        temp[idx] = A[i]
print(len(temp)-1)

max_idx, ans = max(DP) + 1, []
for i in range(N, 0, -1):
    if DP[i] == max_idx-1:
        ans.append(A[i])
        max_idx = DP[i]
print(*ans[::-1])