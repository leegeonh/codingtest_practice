# 문제 1 : 숫자의 합 구하기
'''
N개의 숫자가 공백 없이 써 있다. 이 숫자를 모두 합해 출력하는 프로그램을 작성하시오
'''
i = input()
t = int(input())
sum = 0

while 1:
    sum = sum + t%10

    if t//10 == 0:
        break

    t = t//10

print(sum)

# 문제 1 솔루션
n = input()
numbers = list(input())
sum = 0

for i in numbers:
    sum += int(i)

print(sum)