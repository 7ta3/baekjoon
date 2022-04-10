A = int(input())
B = int(input())
C = int(input())

for i in range(0,10) :
    print(str(A*B*C).count(f'{i}'))