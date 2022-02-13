N = int(input())
r_list = list(map(int, input().split()))

for i in range(1, N):
    max_val = max(r_list[i], r_list[0]); min_val = min(r_list[i], r_list[0])
    while max_val % min_val != 0 :
        max_val , min_val = min_val, max_val % min_val
    A = r_list[0] // min_val
    B = r_list[i] // min_val
    print(f'{A}'+'/'+f'{B}' )