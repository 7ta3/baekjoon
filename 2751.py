import sys

N = int(sys.stdin.readline())
m_list = [0] * 1000001
p_list = [0] * 1000001

lst = []
for _ in range(N):
    a = int(sys.stdin.readline().strip())
    if a < 0 :
        m_list[-a] += 1
    else :
        p_list[a] += 1

for i in range(1000000,0,-1):
    for j in range(m_list[i]):
        print(-i)
for i in range(1000001):
    for j in range(p_list[i]):
        print(i)