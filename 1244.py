N = int(input())
lst = list(map(int, input().split()))
S = int(input())

for _ in range(S):
    s = list(map(int, input().split()))
    if s[0] == 1 :
        for i in range(s[1]-1, N, s[1]):
            lst[i] = 0 if lst[i] == 1 else 1
    else :
        cnt = 0; i = 1; pivot = s[1] - 1
        lst[pivot] = 0 if lst[pivot] == 1 else 1
        while (-1 < pivot-i < N) and (-1 < pivot+i < N) and (lst[pivot-i] == lst[pivot+i]):
            lst[pivot-i] = 0 if lst[pivot-i] == 1 else 1
            lst[pivot+i] = 0 if lst[pivot+i] == 1 else 1
            i += 1
while N > 0 :
    N -= 20
    print(*lst[:20])
    lst = lst[20:]