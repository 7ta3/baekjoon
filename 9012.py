N = int(input())

for _ in range(N):
    temp = []
    a = list(str(input()))
    for i in range(len(a)) :
        temp.append(a.pop())
        while len(temp) > 1 and (temp[-2]==')' and temp[-1] == '('):
            temp.pop()
            temp.pop()
    print('YES' if temp==[] else 'NO')