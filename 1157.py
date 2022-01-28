from re import L


x = input().upper()
alpha_list = []
cnt_list = []

for i in x :
    if i not in alpha_list :
        alpha_list.append(i)
        cnt_list.append(1)
    else :
        for j in range(len(alpha_list)):
            if alpha_list[j] == i :
                cnt_list[j] += 1
if cnt_list.count(max(cnt_list)) > 1 :
    print('?')
else :
    print(alpha_list[cnt_list.index(max(cnt_list))])