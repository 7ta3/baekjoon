costs =[1, 4, 99, 35, 50, 1000]
money = 4578
def solution(money, costs):
    answer = 0
    arr = []
    money_arr = [1, 5, 10, 50, 100, 500]
    for i in range(6):
        arr.append([money_arr[i],costs[i]])
    print(arr)
    arr.sort(key = lambda x: (500//x[0]) * x[1])
    print(arr)
    for i in range(6):
        if money == 0 : break
        cnt = money // arr[i][0]
        money %= arr[i][0]
        answer += cnt * arr[i][1]
    return answer
print(solution(money, costs))