T = int(input())
C = [[7], [2, 4], [1, 3, 5], [2, 6], [1, 5, 7], [2, 4, 6, 8], [3, 5, 9], [4, 8, 0], [5, 7, 9], [6, 8]]

for t in range(T):
    N = int(input())
    DP1 = [1] * 10
    for i in range(1, N):
        DP2 = [0] * 10
        for j in range(10):
            for k in C[j]:
                DP2[k] += DP1[j]
        DP1 = list(DP2)
    print(sum(DP1) % 1_234_567)
