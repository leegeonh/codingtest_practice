# 문제 15 : 수 정렬하기 (버블정렬)
import sys
input = sys.stdin.readline

n = int(input())
numbers = [0] * n

for i in range(n):
    numbers[i] = int(input())

for i in range(n):
    for j in range(n):
        if numbers[i] < numbers[j]:
            temp = numbers[j]
            numbers[j] = numbers[i]
            numbers[i] = temp

for i in range(n):
    print(numbers[i])
