from audioop import reverse


N = [int(i) for i in input()]
N.sort()
for i in N[::-1]:
    print(i, end="")