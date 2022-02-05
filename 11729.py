N = int(input())
pan = [1] * N
dae = [1, 0, 0]

print(2**N - 1)

def hanoi_func(h, a, b, c):
    if h == 1 :
        print(a, c)
    else :
        hanoi_func(h-1, a, c, b)
        print(a, c)
        hanoi_func(h-1, b, a, c)
hanoi_func(N, 1, 2, 3)