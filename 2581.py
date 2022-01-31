M = int(input())
N = int(input())

result = []
for i in range(M,N+1):
    if i == 1:
        continue
    for j in range(2, i) :
        if i % j == 0 :
            break
    else :
        result.append(i)

if bool(result) == False :
    print(-1)
else :
    print(sum(result))
    print(result[0])
