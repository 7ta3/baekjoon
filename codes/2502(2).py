# 1일 : A / 2일 : B / 3일 : A + B / 4일 : A + 2B / 5일 : 2A + 3B / 6일 : 3A + 5B
# -> :PA + QB = K
# QB = K - PA
# B = (K-PA) / Q
# B는 자연수이므로 K-PA는 Q로 나누어 떨어져야 한다.

D, K = map(int, input().split())

one_day_ago = [0, 1]
two_days_ago = [1, 0]
# [A의 계수, B의 계수]

# P, Q값 찾기
for i in range(3, D+1):
    P, Q = one_day_ago[0] + two_days_ago[0], one_day_ago[1] + two_days_ago[1]
    two_days_ago = list(one_day_ago)
    one_day_ago = [P, Q]

# A, B값 찾기
A = 1
while True:
    if not (K - P * A) % Q:
        print(A)
        print((K - P * A) // Q)
        break
    A += 1