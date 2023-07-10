# 문제 2 : 평균구하기
'''
성적의 최댓값을 M이라 할 때 모든 점수를 N / M * 100으로 고친 점수의 평균을 구하는 프로그램을 작성하시오
'''
n = int(input())
grade = list(map(int, input().split()))

max_grade = max(grade)

for i in range(n):
    grade[i] = grade[i] / max_grade * 100

mean = sum(grade) / len(grade)

print(mean)

# 문제 2 solution
n = input()
myList = list(map(int, input().split()))
mymax = max(myList)
sum = sum(myList)

print(sum * 100 / mymax / int(n))
