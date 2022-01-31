T = int(input())

for _ in range(T):
    n = int(input())
    lst = [True] * (n + 1)
    lst[1] = lst[0] = False
    rt = int(n ** (0.5))

    for i in range(2, rt + 1):
        if lst[i] == True :
            for j in range( 2 * i , n + 1, i):
                lst[j] = False

    for i in range(int(n / 2), -1, -1):
        if lst[n - i] == True and lst[i] == True :
            temp = sorted([n-i, i])
            print(temp[0], temp[1])
            break

        
    
