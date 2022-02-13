def com(N,K):
    if N == K or K == 0:
        return 1
    else :
        return (com(N-1, K-1)+com(N-1,K))
N, K = list(map(int,input().split()))

print(com(N,K))