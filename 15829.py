import sys
L = int(sys.stdin.readline())
x = sys.stdin.readline()
alpha = 'abcdefghijklmnopqrstuvwxyz'
sum_val = 0
r = 31
for i in range(L):
    for j in range(26):
        if alpha[j] == x[i]:
            sum_val += (j+1) * (r ** (i))
            break
print(sum_val % 1234567891)
