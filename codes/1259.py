a = input()
while a != '0':
    L = len(a)-1
    for i in range(L+1):
        if a[i] != a[L-i]:
            print('no')
            break
    else :
        print('yes')
    a = input()