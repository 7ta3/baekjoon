N = int(input())

while N != 1 :
    if N == 1:
        break
    for i in range(2,N+1):
        if N % i == 0:
            print(i)
            N //= i
            break