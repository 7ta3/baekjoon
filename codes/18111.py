import sys
N, M, inven = map(int,sys.stdin.readline().split())
field = []
for _ in range(N):
    field.extend(list(map(int,sys.stdin.readline().split())))
field.sort(reverse=True)
min_val = field[-1]
max_val = field[0]
time = 9999999999
height = 0
for i in range(min_val, max_val+1):
    t = 0; B = inven
    for j in range(N*M):
        if field[j] > i :
            B += (field[j] - i)
            t += (field[j] - i) * 2
        elif field[j] < i :
            B -= (i - field[j])
            if B < 0 : t += 9999999999; break
            else : t += (i - field[j])
    if t <= time :
        time = t
        height = i
print(time, height)
