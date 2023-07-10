# 문제 21 : 버블정렬 프로그램 swap 횟수
def merge_sort(arr, count):
    if len(arr) == 1:
        return arr, count
    else:
        arr1, count = merge_sort(arr[:len(arr)//2], count)
        arr2, count = merge_sort(arr[len(arr)//2:], count)

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
            count = count + (len(arr1)-i)
            j += 1

        else:
            lst.append(arr1[i])
            i += 1


    return lst, count

# n = int(input())
# a = list(map(int,input().split()))
n = 8
a = [24,32,42,60,5,15,45,90]

sort_number, count = merge_sort(a, 0)
print(count)