# 문제 9 : DNA 비밀번호(슬라이딩 윈도우)
'''
s : 문자열의 길이 / p : 부분 문자열의 길이 / a, c, g, t : 최소 포함되어야하는 문자의 갯수
임의로 만든 문자열과 비밀번호로 사용할 수 있는 부분 문자열의 길이, 최소 포함되어야하는 문자의 개수가 주어졌을 때
비밀번호의 종류의 수를 구하는 프로그램
'''

s, p = map(int, input().split())
str = input()
acgt = list(map(int, input().split()))
count_acgt = [0] * 4
pointer = 0
cnt = 0

start_str = str[pointer:pointer+p]

count_acgt[0] = start_str.count('A')
count_acgt[1] = start_str.count('C')
count_acgt[2] = start_str.count('G')
count_acgt[3] = start_str.count('T')

if count_acgt[0] >= acgt[0] and count_acgt[1] >= acgt[1] \
        and count_acgt[2] >= acgt[2] and count_acgt[3] >= acgt[3]:
    cnt += 1

for i in range(pointer+p, s):
    if str[i] == 'A':
        count_acgt[0] += 1
    elif str[i] == 'C':
        count_acgt[1] += 1
    elif str[i] == 'G':
        count_acgt[2] += 1
    elif str[i] == 'T':
        count_acgt[3] += 1

    if str[i-p] == 'A':
        count_acgt[0] -= 1
    elif str[i-p] == 'C':
        count_acgt[1] -= 1
    elif str[i-p] == 'G':
        count_acgt[2] -= 1
    elif str[i-p] == 'T':
        count_acgt[3] -= 1

    if count_acgt[0] >= acgt[0] and count_acgt[1] >= acgt[1] \
            and count_acgt[2] >= acgt[2] and count_acgt[3] >= acgt[3]:
        cnt += 1

print(cnt)

# # 문제 9 solution

checkList = [0]*4
myList = [0]*4
cheeckSecret = 0

def myadd(c):
    global checkList, myList, checkSecret

    if c == 'A':
        myList[0] += 1

        if myList[0] == checkList[0]:
            checkSecret += 1
    elif c == 'C':
        myList[1] += 1

        if myList[1] == checkList[1]:
            checkSecret += 1

    elif c == 'G':
        myList[2] += 1

        if myList[2] == checkList[2]:
            checkSecret += 1

    elif c == 'C':
        myList[3] += 1

        if myList[3] == checkList[3]:
            checkSecret += 1
