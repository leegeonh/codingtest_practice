# 문제 8 : 좋은 수 구하기 (투 포인터)
# 순서의 전체 합 -> start와 end가 0에서 시작
# 두 개의 합 -> start : 0 / end : n-1에서 시작
'''
주어진 N개의 수에서 다른 두 수의 합으로 표현되는 수가 있다면 그 수를 '좋은 수'라고 한다.
N개의 수 중 좋은 수가 총 몇개인지 출력하시오.
'''

n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

count = 0

for seq, target in enumerate(numbers):
    if seq < 2:
        continue

    o_point, t_point = 0, seq-1

    while 1:
        sum = numbers[o_point] + numbers[t_point]

        if sum == target:
            count += 1
            break
        elif sum < target:
            o_point += 1
        elif sum > target:
            t_point -= 1

        if o_point >= t_point:
            break

print(count)

# 문제 8 solution
import sys
input = sys.stdin.readline

N = int(input())
result = 0
A = list(map(int, input().split()))
A.sort()

for k in range(N):
    find = A[k]

    i, j = 0, N-1

    while i < j:
        if A[i] + A[j] == find:
            if i != k and j != k:
                result += 1
                break
            elif i == k:
                i += 1
            elif j == k:
                j -= 1

        elif A[i] + A[j] < find:
            i += 1
        else:
            j -= 1

print(result)