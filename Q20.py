# 문제 20 : 수 정렬하기 2 (병합 정렬)

import sys
input = sys.stdin.readline

def merge_sort(arr):
    if len(arr) == 1:
        return arr
    else:
        arr1 = merge_sort(arr[:len(arr)//2])
        arr2 = merge_sort(arr[len(arr)//2:])

    i = 0
    j = 0
    lst = list()

    while 1:
        if len(arr1) == i:
            lst.extend(arr2[j:])
            break
        elif len(arr2) == j:
            lst.extend(arr1[i:])
            break

        if arr1[i] > arr2[j]:
            lst.append(arr2[j])
            j += 1

        else:
            lst.append(arr1[i])
            i += 1


    return lst

n = int(input())
numbers = [0] * n
for i in range(n):
    numbers[i] = int(input())

sort_number = merge_sort(numbers)
print(sort_number)