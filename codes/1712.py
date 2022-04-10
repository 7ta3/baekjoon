A, B, C = list(map(int, input().split()))
if B >= C :
    print(-1)
else :
    print(A // (C - B) if ((A // (C - B)) * (C - B)) > A else A // (C - B) + 1)
