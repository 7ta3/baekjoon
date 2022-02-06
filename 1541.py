eq = list(input())
lst = []
while eq != []:
    num = ''
    while eq[0] != '+' and eq[0] !='-':
        num += eq[0]
        eq = eq[1:]
        if eq == [] :
            break
    lst.append(int(num))
    if eq != [] :
        lst.append(eq[0])
        eq = eq[1:]


i = 0
while '+' in lst:
    if lst[i] == '+':
        sum_v = lst[i-1] + lst[i+1]
        lst.pop(i-1) ; lst.pop(i-1); lst.pop(i-1)
        lst.insert(i-1, sum_v)
    else :
        i += 1
    
i = 0
while '-' in lst:
    if lst[i] == '-':
        sum_v = lst[i-1] - lst[i+1]
        lst.pop(i-1) ; lst.pop(i-1); lst.pop(i-1)
        lst.insert(i-1, sum_v)
    else :
        i += 1
print(lst[0])