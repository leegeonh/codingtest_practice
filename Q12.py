# 문제 12 : 오큰수 구하기 (스택과 큐)
'''
오큰수란 기준점보다 오른쪽에 있으면서 기준점보다 큰 수 중 가장 왼쪽에 있는 수를 의미한다.
이러한 수가 없다면 오큰수는 -1이다. 수열이 주어졌을 때 모든 오큰수를 구하는 프로그램을 작성하시오
'''
n = int(input())
numbers = list(map(int, input().split()))
stack = list()
result = [0] * n

for i in range(n):
    stack.append(i)

    if i == n-1:
        tf = False
    else:
        tf = True

    while stack and tf:
        if numbers[stack[-1]] < numbers[i+1]:
            result[stack[-1]] = numbers[i+1]
            stack.pop()
        else:
            tf = False

for i in stack:
    result[i] = -1

print(result)

# 문제 12 solution

n = int(input())
ans = [0] * n

A = list(map(int, input().split()))
myStack = []

for i in range(n):

    while myStack and A[myStack[-1]] < A[i]:
        ans[myStack.pop()] = A[i]

    myStack.append(i)

while myStack:
    ans[myStack.pop()] = -1

result = ''

for i in range(n):
    result += str(ans[i]) + ' '

print(result)