# 문제 4 : 구간 합 구하기 2
'''
N x N개의 수가 N x N크기의 표에 채워져 있다. X는 행 Y는 열을 의미할때
(X1, Y1)에서 (X2, Y2)의 합을 구하는 프로그램을 작성하시오
'''
import sys
input = sys.stdin.readline

sum = list()

n, m = map(int, input().split())

for _ in range(n):
    temp = list(map(int, input().split()))
    temp_sum = 0
    temp_list = [0]

    # 구간 합 배열 생성
    for i in temp:
        temp_sum += i
        temp_list.append(temp_sum)

    sum.append(temp_list)

# x1, y1, x2, y2 입력
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    if x2 - x1 == 0:
        print(sum[x2-1][y2] - sum[x2-1][y1-1])

    else:
        temp = sum[x1 - 1][y2] - sum[x1 - 1][y1 - 1]

        for i in range(1, x2-x1+1):
            if x2 == x1 + i:
                temp = temp + sum[x2-1][y2] - sum[x2-1][y1-1]
            else:
                temp = temp + sum[x1-1+i][y2] - sum[x1-1+i][y1-1]

        print(temp)

# 문제 4 solution
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

A = [[0] * (n+1)]
D = [[0] * (n+1) for _ in range(n+1)]

for i in range(n):
    A_row = [0] + [int(x) for x in input().split()]
    A.append(A_row)

for i in range(1, n+1):
    for j in range(1, n+1):
        D[i][j] = D[i][j-1] + D[i-1][j] - D[i-1][j-1] + A[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())

    result = D[x2][y2] - D[x1-1][y2] - D[x2][y1-1] + D[x1-1][y1-1]

    print(result)