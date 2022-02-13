N = int(input())

def factorial(N) :
    if N <= 1:
        return 1
    return N * factorial(N-1)

a = factorial(N)
cnt = 0
while a % 10 == 0:
    cnt += 1
    a //= 10
print(cnt)