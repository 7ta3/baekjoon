x = input()
alpha = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
sum = 0
for i in range(len(alpha)) :
    for j in x :
        if j in alpha[i]:
            sum += i+3
print(sum)