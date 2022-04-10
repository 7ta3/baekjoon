N = int(input())

for i in range(1,N) :
    a = i
    lst = []
    while i != 0 :
        lst.append(i % 10)
        i //= 10

    if a + sum(lst) == N :
        print(a)
        break
else:
    print(0)