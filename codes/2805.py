N, M = map(int, input().split())
trees = list(map(int, input().split()))

trees.sort()

start = 0
end = max(trees)
while start<=end:
    mid = (start+end)//2
    temp = 0
    for i in trees:
        if mid < i :
            temp += i - mid
    if temp < M :
        end = mid - 1
    else:
        start = mid + 1
print((start+end)//2)