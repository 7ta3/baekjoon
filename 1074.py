def zigzag(n, x, y):
    global cnt
    if n == 2:
        for i in range(2):
            for j in range(2):
                if y+i == r and x+j == c:
                    return
                else:
                    cnt += 1
    else:
        n //= 2
        if c < n + x and r < n + y: # 1사분면에 있을 때
            zigzag(n, x + 0, y + 0)
        elif n + x <= c and r < n + y: # 2사분면에 있을 때
            cnt += n ** 2
            zigzag(n, x + n, y + 0)
        elif c < n + x and  n + y <= r: # 3사분면에 있을 때
            cnt += (n ** 2) * 2
            zigzag(n, x + 0, y + n)
        elif n + x <= c and n + y <= r: # 4사분면에 있을 때
            cnt += (n ** 2) * 3
            zigzag(n, x + n, y + n)
N, r, c = map(int, input().split())
cnt = 0
zigzag(2**N, 0, 0)
print(cnt)

