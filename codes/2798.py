from itertools import combinations

N, M = map(int, input().split())
lst = list(map(int, input().split()))
sum_lst = list(combinations(lst, 3))
max = 0
for i in sum_lst:
    if max < sum(i) and sum(i) <= M :
        max = sum(i)
print(max)

