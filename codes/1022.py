G = [[0] * 10_001 for _ in range(10_001)]

x, y = 5000, 5000
D = [(1, 0), (0, -1), (-1, 0), (0, 1)]


while True:
    nx = x + D[d][0]
    ny = y + D[d][1]



r1, c1, r2, c2 = map(int, input().split())
