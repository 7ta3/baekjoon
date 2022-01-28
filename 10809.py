x = input()
lst = []
abc = 'abcdefghijklmnopqrstuvwxyz'
for i in abc:
    print(i, len(abc))
    for j in range(len(x)):
        if i == x[j]:
            lst.append(f'{j}')
            break
    else :
        lst.append('-1')
print(' '.join(lst))