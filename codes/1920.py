N = int(input())
A = list(map(int, input().split()))
M = int(input())
lst = list(map(int, input().split()))

A.sort()

for i in lst:
    start = 0
    end = N-1
    while start <= end:
        mid = (start+end)//2
        if A[mid] == i:
            print(1)
            break
        elif A[mid] < i :
            start = mid + 1
        else :
            end = mid - 1
    else:
        print(0)
