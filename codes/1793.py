DP = [0] * 251
for i in range(251):
    if i == 1 or i == 0:
        DP[i] = 1
    elif i == 2:
        DP[i] = 3
    else:
        DP[i] = DP[i-1] + DP[i-2] * 2

while True:
    try:
        n = int(input())
    except:
        break
    print(DP[n])