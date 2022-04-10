N = int(input())
lst = [int(a) for a in input().split()]

new_list = [a/max(lst)*100 for a in lst]
print(sum(new_list)/len(new_list))
