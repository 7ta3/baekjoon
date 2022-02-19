N = int(input())
arr = []
max_y = 0; max_x = 0
for _ in range(N):
    a = list(map(int, input().split()))
    if a[1] > max_y or (a[1] == max_y and a[0] < max_x) :
        max_y = a[1]; max_x = a[0]
    arr.append(a)

arr.sort(key=lambda x: x[0])
max_idx = arr.index([max_x, max_y])
x = arr[0][0]; y = arr[0][1]
width = 0

for i in range(max_idx + 1):
    if y < arr[i][1] :
        width += (arr[i][0] - x) * y
        x = arr[i][0]
        y = arr[i][1]
x = arr[-1][0]; y = arr[-1][1]

for i in range(N-1, max_idx-1, -1):
    if y < arr[i][1] :
        width += (x - arr[i][0]) * y
        x = arr[i][0]
        y = arr[i][1]

if y == max_y and x != max_x :
    width += (x - max_x + 1) * max_y
else :
    width += max_y
print(width)