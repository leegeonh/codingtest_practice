# 문제 10 : 최솟값 찾기1 (윈두우 슬라이싱)
# deque 사용
# n, l = map(int, input().split())
#
# numbers = list(map(int, input().split()))
# min_list = [0] * len(numbers)
#
# # deque -> index left부터 사용 : 순서 - l > pop? value right부터 비교
# for seq, num in enumerate(numbers):
#     pass


# 문제 10 solution
from collections import deque

N, L = map(int, input().split())
mydeque = deque()

now = list(map(int, input().split()))

for i in range(N):
    while mydeque and mydeque[-1][0] > now[i]: # while mydeque : empty -> False / not empty -> True
        mydeque.pop() # pop right

    mydeque.append((now[i], i))

    if mydeque[0][1] <= i - L: # index 비교
        mydeque.popleft()

    print(mydeque[0][0], end=' ')
