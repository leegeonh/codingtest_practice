# 문제 17 : 내림차순으로 자릿수 정렬하기 (선택정렬)
numbers = list(map(int,input()))

for i in range(len(numbers)-1):
    temp = numbers[i+1:]
    number = numbers[i]

    max_num = [numbers[i + 1], i + 1]

    for j in range(len(temp)):
        if max_num[0] < temp[j]:
            max_num[0] = temp[j]
            max_num[1] = i + j + 1

    if numbers[i] < max_num[0]:
        tmp = numbers[i]
        numbers[i] = max_num[0]
        numbers[max_num[1]] = tmp

for i in range(len(numbers)):
    print(numbers[i], end='')


# 문제 17 solution

import sys
print = sys.stdout.write

A = list(input())

for i in range(len(A)):
    Max = i

    for j in range(i+1, len(A)):
        if A[j] > A[Max]:
            Max = j

    if A[i] < A[Max]:
        temp = A[i]
        A[i] = A[Max]
        A[Max] = temp

for i in range(len(A)):
    print(A[i])
