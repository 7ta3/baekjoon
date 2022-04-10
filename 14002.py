import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

DP = [A[0]]

def find(e):
    start = 0
    end = len(DP) - 1
    while start <= end:
        mid = (start + end) // 2
        if DP[mid] == e:
            return mid
        elif DP[mid] < e:
            start = mid + 1
        else:
            end = mid - 1
    return start

for i in A:
    if DP[-1] < i:
        DP.append(i)
    else:
        idx = find(i)
        DP[idx] = i

print(len(DP))