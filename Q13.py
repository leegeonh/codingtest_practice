# 문제 13 : 카드 게임 (스택과 큐)
'''
N장의 카드가 1번카드가 제일 위에 N이 가장 아래인 상태로 놓여져 있다.
가장 먼저 위에 있는 카드를 버리고  그 다음 가장 위에 있는 카드를 가장 아래로 옮긴다.
가장 마지막에 남는 카드를 구하는 프로그램을 작성하시오
'''

from collections import deque

n = int(input())
card = deque(i for i in range(n,0,-1))

while len(card) != 1:
    card.pop()
    card.appendleft(card.pop())

print(card[0])


# 문제 13 solution

from collections import deque

N = int(input())
myQueue = deque(i for i in range(1, N+1))

while len(myQueue) > 1:
    myQueue.popleft()
    myQueue.append(myQueue.popleft())

print(myQueue[0])