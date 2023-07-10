# 문제 5 : 나머지 합 구하기
'''
N개의 수가 주어졌을 때 연속된 부분의 합이 M으로 나누어 떨어지는 구간의 개수를 구하는 프로그램
'''

n, m = map(int, input().split())

numbers = list(map(int, input().split()))
sum_list = list()
temp = 0

# 합 배열 생성
for i in numbers:
    temp = temp + i
    sum_list.append(temp)

# 입력된 값 하나로 m값이 나누어 지는 갯수
count_1 = 0
for i in numbers:
    if i % m == 0:
        count_1 += 1

# idea : (a + b) / c = (a / c) + (b / c)
# 각 배열 합의 나머지가 0인 값들 2개를 뽑아서 갯수 count
count = 0
for i in sum_list:
    if i % m == 0:
        count += 1

# count_1 + nC2)
print(int(count * (count-1) / 2 + count) + count_1)


# 문제 5 solution

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

A = list(map(int, input().split()))
S = [0] * n
C = [0] * m
S[0] = A[0]
answer = 0

for i in range(1, n):
    S[i] = S[i-1] + A[i] # 합 배열 저장

for i in range(n):
    remainder = S[i] % m
    if remainder == 0: # 0 - i 까지의 구간 합 자체가 0일때 정답에 더하기
        answer += 1
    C[remainder] += 1 # 나머지가 같은 인덱스의 개수 값 증가

for i in range(m):
    # 나머지가 같은 인덱스 중 2개를 뽑는 경우의 수를 더하기
    if C[i] > 1:
        answer += (C[i] * (C[i] - 1) // 2)


print(answer)
