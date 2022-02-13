import sys
N = int(sys.stdin.readline())

stack = []
here = 0
print_list =[]
for i in range(N):
    a = int(sys.stdin.readline())
    while here < a :
        here += 1
        stack.append(here)
        print_list.append('+')
    if stack[-1] == a :
        stack.pop()
        print_list.append('-')
    else :
        print('NO')
        break
    
else:
    for i in print_list : print(i)

