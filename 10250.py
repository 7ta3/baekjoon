import sys

T = int(input())
for i in range(T):
    H, W, N = list(map(int, sys.stdin.readline().split()))
    if N%H == 0 :
        print(f'{H}'+ '0'*(2-len(str(N//H)))+f'{N//H}')
    else :
        print(f'{N%H}'+ '0'*(2-len(str(N//H+1)))+f'{N//H+1}')