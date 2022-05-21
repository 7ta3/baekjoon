from collections import deque
n, w, L = map(int, input().split())
A = deque(list(map(int, input().split())))
D = deque([0] * w)
T = 0
while A or 0 < sum(D):
    D.rotate(1)
    D[-1] = 0
    if A and (sum(D) + A[0] <= L):
        D[-1] = A[0]
        A.popleft()
    T += 1
print(T)