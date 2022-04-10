from collections import deque

N = int(input())
cards = deque()

for i in range(1,N+1):
    cards.append(i)
while len(cards) != 1 :
    cards.popleft()
    a = cards.popleft()
    cards.append(a)
print(cards[0])