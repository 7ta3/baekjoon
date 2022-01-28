N = int(input())

for i in range(N):
    C = input()
    sum = cont = 0
    for j in range(0, len(C)):
        if C[j] == 'O':
            cont += 1
            sum += cont
            before = C[j]
        else:
            cont = 0
    print(sum)
