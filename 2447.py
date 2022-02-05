N = int(input())

def star_func(N):
    if N < 4 :
        return ['***'], ['* *']
    else :
        a, b = star_func(N//3)
        c = []
        d = []
        for i in range(N//9) : c.append(a[i] * 3)
        for i in range(N//9) : c.append(b[i] * 3)
        for i in range(N//9) : c.append(a[i] * 3)

        for i in range(N//9): d.append(a[i] + ' ' * (N // 3) + a[i])
        for i in range(N//9): d.append(b[i] + ' ' * (N // 3) + b[i]) 
        for i in range(N//9): d.append(a[i] + ' ' * (N // 3) + a[i]) 

        return c, d

x, y = star_func(N)
for i in x :
    print(i)
for i in y :
    print(i)
for i in x:
    print(i)
