x = input()
N = 0
if len(x) == 1 :
    x = '0'+ x

sum_num = str(int(x[0]) + int(x[1]))
if len(sum_num) == 1 :
    sum_num = '0'+ sum_num

new_num = str(x[-1]) + str(sum_num[-1])
if len(new_num) == 1 :
    new_num = '0'+ new_num
N += 1
while x != new_num : 
    sum_num = str(int(new_num[0]) + int(new_num[1]))
    if len(sum_num) == 1 :
        sum_num = '0'+ sum_num

    new_num = str(new_num[-1]) + str(sum_num[-1])
    if len(new_num) == 1 :
        new_num = '0'+ new_num
    N += 1
print(N)