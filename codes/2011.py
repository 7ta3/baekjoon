N = 'a' + input()
DP = [0] * len(N)

for i in range(len(N)):
    if i == 0 or i == 1:
        if N[i] == '0': # 0으로 시작하는 경우 error
            print(0)
            exit(0)
        DP[i] = 1

    else:
        if int(N[i-1]+N[i]) <= 26:
            if int(N[i-1]+N[i]) == 0: # 0이 연속으로 오는 경우 error
                print(0)
                exit(0)
            if N[i] == '0': # 0인데 앞자리 숫자로 묶어서 알파벳을 나타낼 수 있는 경우
                DP[i] = DP[i - 2] % 1000000
            elif N[i-1] == '0': # 0 뒷자리는 앞자리와 묶을 수 없으므로
                DP[i] = DP[i - 1] % 1000000
            else:
                DP[i] = (DP[i - 2] + DP[i - 1]) % 1000000
        elif N[i] == '0': # 0인데 앞자리 숫자로 묶어서 나타낼 수 없는 경우
            print(0)
            exit(0)
        else:
            DP[i] = (DP[i - 1]) % 1000000
print(DP[-1])