def N_Queen(idx):
    for i in range(N):
        for j in range(idx):
            if i == V[j] or abs(i - V[j]) == abs(idx - j):
                break
        else:
            if idx + 1 == N:
                global ans
                ans += 1
                return

            V[idx] = i
            N_Queen(idx + 1)

N = int(input())
ans = 0
V = [0] * N
N_Queen(0)
print(ans)
