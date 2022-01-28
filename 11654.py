x = input()
lst = []
for i in 'abcdefghijklmnopqrstuvwxyz' :
    for j in range(len(x)) :
        if x[j] == i :
            lst.append(f'{j}')
        else :
            lst.append('-1')
print(' '.join(lst))