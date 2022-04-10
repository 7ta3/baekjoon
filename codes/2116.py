N = int(input())
dices = []
for _ in range(N):
    dices.append(list(map(int, input().split())))

def max_func(arr, N):
    i = arr.index(N)
    if i == 0:
        top = arr[5]
        del arr[5]
    elif i == 1:
        top = arr[3]
        del arr[3]
    elif i == 2:
        top = arr[4]
        del arr[4]
    elif i == 3:
        top = arr[1]
        del arr[1]
    elif i == 4:
        top = arr[2]
        del arr[2]
    elif i == 5:
        top = arr[0]
        del arr[0]
    arr.remove(N)
    return max(arr), top

ans = 0
for i in range(1,7):
    temp = 0
    dice = list(dices[0])
    max_val, top = max_func(dice, i)
    temp += max_val
    for j in range(1, N):
        dice = list(dices[j])
        max_val, top = max_func(dice, top)
        temp += max_val
    ans = max(ans, temp)
print(ans)