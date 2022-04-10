T = int(input())

for _ in range(T):
    A, B = list(map(int,input().split()))
    max_val = max(A,B); min_val = min(A, B)
    if A == B :
        print(A)
        continue
    while True :
        if max_val % min_val == 0 : break
        max_val, min_val = min_val, max_val % min_val
    print(A * B // min_val)