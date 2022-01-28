import math
N = int(input())
max_5 = N // 5
reminder = N % 5
if reminder % 3 == 0 :
    print(max_5 + (reminder // 3))
else:
    for i in range(max_5):
        max_5 -= 1
        reminder += 5
        if reminder % 3 == 0 :
            print(max_5 + (reminder // 3))
            break
    else :
        print(-1)

