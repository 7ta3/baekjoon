C = int(input())

for i in range(C):
    lst = [int(a) for a in input().split()]
    print(lst)
    avg_std = sum(lst[1:])/lst[0]
    cnt = 0
    for j in lst[1:] :
        if j > avg_std:
            cnt += 1
    print('%0.3f%%'%(round(cnt/lst[0]*100,3)))