# 문제 16 : 버블정렬 프로그램 1

n = int(input())
numbers = [0] * n

for i in range(n):
    num = int(input())
    numbers[i] = (num, i)

numbers.sort()

sort_idx = [0] * n

for i in range(n):
    sort_idx[i] = numbers[i][1] - i

print(max(sort_idx)+1)


# 문제 16 solution

import sys
input = sys.stdin.readline

N = int(input())
A = list()

for i in range(N):
    A.append((int(input()), i))

Max = 0
sorted_A = sorted(A)

for i in range(N):
    if Max < sorted_A[i][1] - i:
        Max = sorted_A[i][1] - i

print(Max+1)