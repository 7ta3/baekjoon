a, b = map(str, input().split())
a_r = a[::-1]
b_r = b[::-1]
if int(a_r) > int(b_r):
    print(a_r)
else :
    print(b_r)
