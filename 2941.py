x = input()
cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
cnt = 0
for i in cro:
    while i in x :
        x = x.replace(i," ",1)
        cnt += 1

print(len(x.replace(" ",""))+cnt)