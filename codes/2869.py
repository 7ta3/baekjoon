import math
A, B, V = list(map(int, input().split()))
Q = (V - A) // (A - B)
R = (V - A) % (A - B)
print(Q + 1 if R + A <= A else Q + 2)