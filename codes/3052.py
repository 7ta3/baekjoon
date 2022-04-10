lst = []
for i in range (10):
    A = int(input())%42
    lst.append(A)
print(len(set(lst)))
