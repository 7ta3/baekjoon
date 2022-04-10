lst = list(map(int, input().split()))

def ascending(arr):
    for i in range(8):
        if arr[i] != (i+1):
            return False
    return True

def descending(arr):
    for i in range(8):
        if arr[i] != (8-i):
            return False
    return True

if ascending(lst) == True:
    print('ascending')
elif descending(lst) == True:
    print('descending')
else:
    print('mixed')