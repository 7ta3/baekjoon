n = int(input())

while n != 0 :
    rt = int((2 * n + 1) ** (0.5))
    lst = [True for i in range(2 * n + 1)]
    lst[1] = False
    for i in range(2, rt + 1) :
        if lst[i] == True :
            for j in range(2 * i, 2 * n + 1, i):
                lst[j] = False
    print(lst[n + 1: 2 * n + 1].count(True))
    n = int(input())
