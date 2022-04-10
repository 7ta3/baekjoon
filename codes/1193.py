X = int(input())

cnt = 0
line = 0
while X > 0 :
    line += 1
    X -= line
X += line

if line % 2 :
    print(f'{line-X+1}/{X}')
else :
    print(f'{X}/{line-X+1}')