N1 = int(input())
ans = list([N1])
for N2 in range(N1+1):
    temp = list([N1])
    temp.append(N2)
    i = N1; j = N2
    while i-j >= 0:
        temp.append(i-j)
        i, j = j, i-j
    if len(temp) > len(ans) :
        ans = temp
print(len(ans))
print(*ans)

