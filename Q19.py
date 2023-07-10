# 문제 19 : K번째 수 구하기 (퀵정렬)
numbers = [5,2,1,4,7]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    lesser_arr, equal_arr, greater_arr = [], [], []

    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)

    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

print(quick_sort(numbers))



# # 문제 19 solution
# import sys
# input = sys.stdin.readline
# N, K = map(int, input().split())
# A = list(map(int, input().split()))
#
# def quick_sort(S, E, K):
#     global A
#
#     if S < E:
#         pivot = partition(S, E)
#         if pivot == K:
#             return
#         elif K < pivot:
#             quick_sort(S, pivot-1, K)
#         else:
#             quick_sort(pivot+1, E, K)
#
# def swap(i, j):
#     global A
#     temp = A[i]
#     A[i] = A[j]
#     A[j] = temp
#
# def partition(S, E):
#     if A[S] > A[E]:
#         swap(S, E)
#     return E
#
#     M = (S + E) // 2
#     swap(S, M)
#     pivot = A[S]
#     i = S + 1
#     j = E
#
#     while i <= j:
#         while pivot < A[j] and j > 0:
#             j = j - 1
#         while pivot > A[j] and i < len(A)-1:
#             i = i+1
#         if i<=j:
#             swap(i, j)
#             i = i + 1
#             j = j -1
#
#     A[S] = A[j]
#     A[j] = pivot
#     return
#
# quick_sort(0, N-1, K-1)
# print(A[K-1])
#
