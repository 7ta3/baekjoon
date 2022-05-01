import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # 세로, 가로
old = [list(map(int, input().split())) for _ in range(N)]
new = [list(map(int, input().split())) for _ in range(N)]

'''
두 개를 동시에 체크 (for문)
둘이 다른 숫자가 나오면 그때 dfs로 영역 찾아 old와 같은 숫자로 바꿔주기
다른 숫자가 한 번 더 나오면 그때는 false
한 번만 나오거나 아예 안 나오면 true

'''

def dfs(r, c):

    ST = [(r, c)]
    tar = new[r][c]
    org = old[r][c]
    old[r][c] = tar
    visit = {(r, c)}

    while ST:
        curR, curC = ST.pop()

        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            newR, newC = curR + dr, curC + dc
            if 0 <= newR < N and 0 <= newC < M and old[newR][newC] == org and \
                    (newR, newC) not in visit:
                ST.append((newR, newC))
                old[newR][newC] = tar
                visit.add((newR, newC))


def isCPCU():

    cnt = 0
    for row in range(N):
        for col in range(M):
            if old[row][col] != new[row][col]:
                # if new[row][col]:
                dfs(row, col)
                cnt += 1
                # print(row, col)
                if cnt > 1: return False

    return True

# print(old, new)
if isCPCU(): print('YES')
else: print('NO')