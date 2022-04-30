N = int(input())
L = list(map(int, input().split()))

DP = [0]
for i in range(N):
    if L[i] > DP[-1]:
        DP.append(L[i])
    else:
        flag = False
        for j in range(1, len(DP)):
            if flag:
                break
            for k in range(i):
                if DP[j] == L[k] and DP[j] > L[i]:
                    flag = True
                    DP[j] = L[i]
                    break
print(len(DP)-1)