N = int(input())
def factorial_func(N):
    if N < 2 :
        return 1
    else :
        return N * factorial_func(N-1)
result = factorial_func(N)
print(result)