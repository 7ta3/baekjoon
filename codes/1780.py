def paper(arr, N):
    a = arr[0][0]
    for i in range(N):
        for j in range(N):
            if arr[j][i] != a:
                N //= 3
                for x in range(3):
                    for y in range(3):
                        temp_arr = []
                        for k in range(N):
                            temp_arr.append(arr[N*y+k][N*x:N*(x+1)])
                        paper(temp_arr, N)
                return
    global lst
    lst[a+1] += 1
    return a

n = int(input())
A = []
lst = [0] * 3
for _ in range(n):
    A.append(list(map(int, input().split())))
paper(A, n)
for i in lst:
    print(i)