# 문제 3 : 구간 합
'''
수 N개가 주어졌을 때 i번째 수에서 j번째 수까지의 합을 구하는 프로그램을 작성하시오
'''
n, m = map(int, input().split())
sum_list = [0] * (n+1)

numbers = list(map(int, input().split()))

    # 합 배열 만들기
for i in range(n):
    sum_list[i+1] = sum_list[i] + numbers[i]

    # 합 배열을 이용한 구간 합 구하기
for i in range(m):
    s, e = map(int, input().split())
    print(sum_list[e] - sum_list[s-1])

# 문제 3 solution
import sys
input = sys.stdin.readline # 반복문으로 여러줄을 입력받는 상황에서 사용하지 않으면 timeover가 발생할 수 있음

suNo, quizNo = map(int, input().split())
numbers = list(map(int, input().split()))

prefix_sum = [0]
temp = 0

    # 합배열 만들기
for i in numbers:
    temp = temp + i
    prefix_sum.append(temp)

    # 합 배열을 이용한 구간 합 구하기
for i in range(quizNo):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s-1])