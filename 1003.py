T = int(input())

for _ in range(T):
    N = int(input())
    dp_0 = [0] * (N+1)
    dp_1 = [0] * (N+1)
    for i in range(N+1):
        if i == 0 :
            dp_0[i] += 1
        elif i == 1:
            dp_1[i] += 1
        else :
            dp_0[i] = dp_0[i-1]+dp_0[i-2]
            dp_1[i] = dp_1[i-1]+dp_1[i-2]
    print(dp_0[-1], dp_1[-1])