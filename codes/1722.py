from itertools import permutations
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

def func(arr, n, sum_val, num):
    print(n, sum_val, num, arr)
    if n < 1 or N < sum_val or N < num:
        return

    temp = 1
    for i in range(1, n+1):
        temp *= i
    print(temp)

    if N < temp:
        arr.append(num)
        func(arr, n-1, sum_val, 1)

    else:
        sum_val += temp

        if sum_val == N:
            global ans
            arr.append(num)
            ans = arr
            return True

        func(arr, n, sum_val, num+1)

ans = []
if A[0] == 1:
    ans = func([], N-1, 0, 1)
    print(*ans)

else:
    numbers = A[1:]

