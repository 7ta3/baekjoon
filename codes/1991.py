def preorder(root):
    global ans
    ans += root

    if G[root][0] != '.':
        preorder(G[root][0])

    if G[root][1] != '.':
        preorder(G[root][1])

def inorder(root):
    global ans
    if G[root][0] != '.':
        inorder(G[root][0])

    ans += root

    if G[root][1] != '.':
        inorder(G[root][1])

def postorder(root):
    global ans
    if G[root][0] != '.':
        postorder(G[root][0])

    if G[root][1] != '.':
        postorder(G[root][1])

    ans += root

N = int(input())
G = dict()
for i in range(N):
    l = list(map(str, input().split()))
    G[l[0]] = []
    for j in l[1:]:
        G[l[0]].append(j)

ans = ''
preorder('A')
print(ans)
ans = ''
inorder('A')
print(ans)
ans = ''
postorder('A')
print(ans)