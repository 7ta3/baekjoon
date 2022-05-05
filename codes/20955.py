from collections import deque, defaultdict
N, M = map(int, input().split())
G = defaultdict(list)
for _ in range(M):
    u, v = map(int, input().split())
    G[u].append(v)
    G[v].append(u)

cnt = -1
edge = 0
V = [False] * (N+1)
for i in range(1, N+1):
    if not V[i]:
        cnt += 1
        Q = deque([i])
        V[i] = True
        while Q:
            node = Q.popleft()
            for n in G[node]:
                if not V[n]:
                    Q.append(n)
                    V[n] = True
                    edge += 1
print(cnt + M - edge)
'''
    o
   / \
 o ㅡㅡ o
이런 식으로 연결 된 경우가 있을 때 연결된 두 뉴런을 끊어 주어 트리 형태를 만드는 작업이 필요
따라서 전체 간선의 수에 필요한 간선의 수를 빼서 몇 번 잘라야 하는지 체크
'''