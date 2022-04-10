N = int(input())
M = int(input())
init = 100
remote = [1] * 10
if M > 0 :
    for i in list(map(int, input().split())):
        remote[i] = 0
# 리모컨 버튼이 고장나지 않았을 수도 있음

min_val = abs(N-init)
# +, -로만 이동했을 경우

for i in range(N + min_val + 1):
    val = [int(j) for j in list(str(i))]
    # i를 각각 쪼갬 ( 73 -> 7,3)
    for j in val:
        if remote[j] != 1:
            break
    else:
    # 리모컨으로 이동이 가능한 경우 해당 채널로부터 N까지 거리(+,-로 이동하는 거리) + 해당 채널로 이동하기 위해 누른 버튼 수
    # min_val update
        min_val = min(min_val, abs(i-N) + len(val))
print(min_val)


