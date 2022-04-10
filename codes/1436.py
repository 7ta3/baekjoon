N =int(input())
cnt = 1
val = 666

while cnt != N :
    val += 1
    lst = list(str(val))
    sixs = 0
    for i in range(1, len(lst)):
        if lst[i-1] == lst[i] == '6':
            sixs += 1
            if sixs == 2 :
                cnt += 1
                break
        else:
            sixs = 0
print(val)