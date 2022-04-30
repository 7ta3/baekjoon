import sys
input = sys.stdin.readline

N = int(input())
L = list(map(int, input().split()))

ans = 0
temp = 0
for i in range(N-1):
    temp = ((temp + 1) * L[i]) % (10 ** 9 + 7)
    ans += temp
    ans %= 10 ** 9 + 7
print(ans)

