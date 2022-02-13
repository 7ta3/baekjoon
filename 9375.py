N = int(input())
for _ in range(N):
    T = int(input())
    dic = {}
    for _ in range(T):
        new = input().split()
        if new[-1] not in dic.keys() :
            dic[new[-1]] = [new[0]]
        elif new[-1] in dic.keys():
            if new[0] not in dic.values():
                dic[new[-1]].append(new[0])
    key_list = list(dic.keys())
    result = 1
    for i in key_list: result *= (len(dic[i]) + 1)
    print(result-1)