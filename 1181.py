import sys

N = int(sys.stdin.readline())
str_list =[]
alpha = 'abcdefghijklmnopqrstuvwxyz'
for _ in range(N):
    str_list.append(str(sys.stdin.readline().strip()))
str_list = list(set(str_list))
str_list.sort()
str_list.sort(key = lambda a : len(a))
for i in str_list:
    print(i)