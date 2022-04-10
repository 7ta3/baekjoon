import sys
N = int(input())
meetings = []
times = []
for _ in range(N):
    meetings.append(list(map(int, sys.stdin.readline().split())))

meetings.sort()
meetings.sort(key=lambda x : x[1])

lst = []
for i in range(len(meetings)):
    if i == 0 :
        lst.append(meetings[i])
    else :
        if lst[-1][1] <= meetings[i][0]:
            lst.append(meetings[i])

print(len(lst))
    