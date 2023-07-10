# 문제 6 : 연속된 자연수의 합 구하기(투 포인터)
'''
어떠한 자연수 N은 몇 개의 연속된 자연수의 합으로 나타낼 수 있다. 어떤 자연수 N을 몇 개의 연속된 자연수의 합으로
나타내는 가짓수를 알고 싶다. 이때 사용하는 자연수는 N이여야 한다. (ex 15 -> 15, 7+8, 4+5+6, 1+2+3+4+5 => 4가지)
N을 입력받아 연속된 자연수의 합으로 나타내는 가짓수를 출력하는 프로그램을 작성하시오
'''

n = int(input())
numbers = [x for x in range(1, n//2 + 2)]
print(numbers)

s_point, e_point = 0, 1
count = 1

while 1:
    add = sum(numbers[s_point:e_point]) # 더하기 연산을 계속해서 하지않고 구현
    if n == add:
        count += 1
        e_point += 1
    elif n > add:
        e_point += 1
    elif n < add:
        s_point += 1

    if e_point > len(numbers):
        break

print(count)


# 문제 6 solution
# sum > N : sum = sum - start_index; start_index ++
# sum < N : end_index ++ ; sum = sum + end_index
# sum == N : end_index ++; sum = sum + end_index; count ++

n = int(input())
count = 1
start_index = 1
end_index = 1
sum = 1

while end_index != n:
    if sum == n:
        count += 1
        end_index += 1
        sum += end_index
    elif sum > n:
        sum -= start_index
        start_index += 1
    else:
        end_index += 1
        sum += end_index

print(count)