# 문제 18 : ATM 인출 시간 계산하기 (삽입정렬)
n = int(input())
customer_time = list(map(int,input().split()))
insert = list()

for i in range(n):
    insert.append(customer_time[i])

    for j in range(i):
        if j == 0 and insert[j] >= insert[i]:
            temp_list = [insert[i]]
            temp_list.extend(insert[:i])
            insert = temp_list

        elif j != 0 and insert[j-1] < insert[i] <= insert[j]:
            temp_list = insert[:j]
            temp_list.append(insert[i])
            temp_list.extend(insert[j:i])
            insert = temp_list

# 누적 합
add_list = [insert[0]]
for i in range(1, n):
    add_list.append(add_list[i-1]+insert[i])

print(sum(add_list))


# 문제 18 solution

N = int(input())
A = list(map(int, input().split()))
S = [0] * N

for i in range(1, N):
    insert_point = i
    insert_value = A[i]

    for j in range(i-1, -1, -1):
        if A[j] < A[i]:
            insert_point = j+1
            break

        if j == 0:
            insert_point = 0

    for j in range(i, insert_point, -1):
        A[j] = A[j-1]

    A[insert_point] = insert_value

S[0] = A[0]

for i in range(1, N):
    S[i] = S[i-1] + A[i]

sum = 0

for i in range(0, N):
    sum += S[i]

print(sum)