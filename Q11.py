# 문제 11 : 스택으로 수열 만들기 (스택과 큐)
'''
스택에 push 하는 순서는 반드시 오름차순을 지키도록 가정하며, 수열이 주어졌을 때 이러한 방식으로 스택을
이용해 주어진 수열을 만들 수 있는지 확인하고 만들 수 있다면 어던 순서로 push와 pop을 수행하여야 하는지
확인하는 프로그램을 작성해보자 출력이 불가능한 때에는 NO를 출력한다.
'''
from collections import deque

n = int(input())
series = deque()
stack = list()
push_pop = ''
i = 0

for _ in range(n):
    series.append(int(input()))

while series:
    i += 1
    stack.append(i)
    push_pop += '+\n'

    while len(stack) != 0:

        if series[0] == stack[-1]:
            stack.pop()
            series.popleft()
            push_pop += '-\n'

        elif series[0] > stack[-1]:
            break

        elif series[0] < stack[-1]:
            push_pop = 'NO'
            break

    if 'NO' in push_pop:
        break

if 'NO' in push_pop:
    print('NO')
else:
    for i in push_pop:
        print(i)


# 문제 11 solution

N = int(input())
A = [0] * n

for i in range(N):
    A[i] = int(input())

stack = []
num = 1
result = True
answer = ""

for i in range(N):
    su = A[i]
    if su >= num:
        while su >= num:
            stack.append(num)
            num += 1
            answer += '+\n'
        stack.pop()
        answer += '-\n'
    else:
        n = stack.pop()
        if n > su:
            print('NO')
            result = False
            break
        else:
            answer += '+\n'

if result:
    print(answer)