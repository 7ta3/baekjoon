import sys
N = int(sys.stdin.readline())

def check(arr, cnt):
    L = len(arr)
    val = arr[0][0]
    ans = True
    for i in range(L):
        for j in range(L):
            if arr[i][j] != val:
                ans = False
    if ans == False :
        arr1 = []; arr2 =[]; arr3=[]; arr4=[]
        for i in range(L//2):
            arr1.append(arr[i][:L//2])
            arr2.append(arr[i][L//2:])
            arr3.append(arr[L//2+i][L//2:])
            arr4.append(arr[L//2+i][:L//2])
        check(arr1, cnt); check(arr2, cnt); check(arr3, cnt); check(arr4, cnt)

    if ans == True :
        cnt[val] += 1

arr = []
for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))
cnt = [0,0]
check(arr, cnt)
print(cnt[0])
print(cnt[1])