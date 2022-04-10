K, N = map(int,input().split())
lines = []
for _ in range(K):
    lines.append(int(input().strip()))
end = max(lines)
start = 1
mid = (start + end) // 2
temp = -1
while start <= end:
    mid = (end + start) // 2
    cnt = 0
    for i in lines:
        cnt += i // mid
    if cnt < N :
        end = mid - 1
    else :
        start = mid + 1
print(end)