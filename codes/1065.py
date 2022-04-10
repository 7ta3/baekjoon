def han_num(x) :
    x_st = str(x)
    if x >= 10 :
        diff = int(x_st[0]) - int(x_st[1])
        for i in range(1,len(x_st)) :
            if int(x_st[i-1]) - int(x_st[i]) == diff :
                pass
            else :
                return False
        return True
    else :
        return True


N = int(input())
lst = [a for a in range(1,N+1) if han_num(a)]
print(len(lst))