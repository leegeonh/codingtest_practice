# 문제 24 : 신기한 소수 찾기
import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n = int(input())
odds = [1, 3, 5, 7, 9]

def DFS(num, digit):
    num = num * 10
    digit += 1
    for odd in odds:
        number = num + odd
        prime = True

        for i in range(2, number//2+2):
            if number % i == 0:
                prime = False
                break

        if digit == n and prime is True:
            print(number)

        if digit != n and prime is True:
            DFS(number, digit)

DFS(2, 1)
DFS(3, 1)
DFS(5, 1)
DFS(7, 1)

#  문제 24 solution

# import sys
# sys.setrecursionlimit(10000)
# input = sys.stdin.readline
# n = 6
#
# def isPrime(num):
#     for i in range(2, int(num/2+1)):
#         if num%i == 0:
#             return False
#     return True
#
# def DFS(number):
#     if len(str(number)) == n:
#         print(number)
#     else:
#         for i in range(1, 10):
#             if i % 2 == 0: # 짝수라면 더는 탐색 불필요
#                 continue
#             if isPrime(number * 10 + i): # 소수이면 자릿수 늘림
#                 DFS(number * 10 + i)
#
# DFS(2)
# DFS(3)
# DFS(5)
# DFS(7)
