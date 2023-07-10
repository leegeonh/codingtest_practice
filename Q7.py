# 문제 7 : 주몽의 명령(투 포인터)
'''
2개의 수를 합쳐 M이 되면 갑옷이 만들어진다.
재료가 N개 있을 때 몇개의 갑옷을 만들 수 있는지를 구하는 프로그램을 작성하시오
'''

n = int(input())
m = int(input())

materials = list(map(int, input().split()))

materials = sorted(materials)

o_point, t_point = 0, 1
sum = 0
count = 0

while 1:
    sum = materials[o_point] + materials[t_point]

    if sum == m:
        count += 1
        o_point += 1
        t_point = o_point + 1
    elif sum < m:
        if t_point == n-1:
            o_point += 1
            t_point = o_point + 1
        else:
            t_point += 1
    elif sum > m:
        o_point += 1
        t_point = o_point + 1

    if t_point >= n - 1 & o_point >= n - 2:
        sum = materials[o_point] + materials[t_point]
        if sum == m:
            count += 1

        break

print(count)

# 문제 7 solution
# start_point -> 0 / end_point -> n-1

n = int(input())
m = int(input())

numbers = list(map(int, input().split()))
numbers.sort()

start_point, end_point = 0, n-1
count = 0

while 1:
    sum = numbers[start_point] + numbers[end_point]

    if sum == m:
        count += 1
        start_point += 1
        end_point -= 1
    elif sum < m:
        start_point += 1
    elif sum > m:
        end_point -= 1

    if start_point >= end_point:
        break

print (count)