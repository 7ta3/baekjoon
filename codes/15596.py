def d(n):
    sum = 0
    n_mod = n
    while n_mod > 0 :
        sum += n_mod % 10
        n_mod//= 10
    return n + sum

kap_num = []
i = 1
while i <= 10000 :
    kap_num.append(d(i))
    i += 1
lst = [a for a in range(1,10001)]
num = [int(a) for a in lst if a not in kap_num]
for i in num :
    print(i)