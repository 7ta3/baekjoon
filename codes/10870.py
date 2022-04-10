N = int(input())

def fibo_func(N):
    if N < 2 :
        return N
    else :
        return fibo_func(N-1) + fibo_func(N-2)

result = fibo_func(N)
print(result)