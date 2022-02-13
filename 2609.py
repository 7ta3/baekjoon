A, B = list(map(int,input().split()))
min_val = 1
i = 2

while True:
    if i > A or i > B :
        break
    if A % i == 0 and B % i == 0:
        min_val *= i
        A //= i
        B //= i
    else:
        i += 1
print(min_val)
print(min_val * A * B)