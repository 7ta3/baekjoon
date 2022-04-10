import sys
input = sys.stdin.readline
N = int(input())
E = 2 * N + 1
M = int(input())
A = input() + ' '
cnt = 0
IOI = 0
temp = 0
def chg(val):
    if val == 'I':
        return 'O'
    else:
        return 'I'

for i in range(M+1):
    if temp == 0:
        if A[i] == 'I':
            temp = 'O'
            IOI = 1
        else:
            continue
    else:
        if temp == A[i]:
            temp = chg(temp)
            IOI += 1
        else:
            cal = IOI - (2 * N + 1)
            if cal >= 0:
                cnt += cal // 2 + 1
            if A[i] == 'I':
                IOI = 1
                temp = 'O'
            else:
                IOI = 0
                temp = 0
print(cnt)