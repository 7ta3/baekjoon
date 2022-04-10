dic = {0:'000', 1:'001', 2:'010', 3:'011', 4:'100', 5:'101', 6:'110', 7:'111'}
A = input()
ans = ''
for i in A:
    ans += dic[int(i)]

if len(ans) == 3 and ans == '000':
    print(0)
    exit(0)

for i in range(len(ans)):
    if ans[i] != '0':
        print(ans[i:])
        break
