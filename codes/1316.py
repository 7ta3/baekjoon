N = int(input())
cnt = 0
for _ in range(N) :
    lst = []
    x = input()
    for i in x :
        if i not in lst :
            lst.append(i)
        else :
            if lst[-1] != i :
                break
    else :
        cnt += 1
print(cnt)
