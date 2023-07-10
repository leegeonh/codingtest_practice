# 문제 14 : 절댓값 힙 구현 (스택과 큐)
'''
절댓값 힙은 다음과 같다.

배열에 정수를 넣는다
-> 배열에서 절댓값이 가장 작은 값을 출력한 후 그 값을 배열에서 제거한다.
-> 절댓값이 가장 작은 값이 여러개일 경우에는 그 중 가장 작은 수를 출력하고 배열에서 제거한다.

절댓값 힙을 구현하시오 단 input 값이 0 일 때 절댓값이 가장 작은 수를 출력하고 그 값 제거
'''
n = int(input())

plus_heap = [0]
minus_heap = [0]
string = ''

def min_heap_insert(arr, number):
    insert = len(arr)
    arr.append(number)

    while insert != 1:
        if arr[insert//2] > arr[insert]:
            tmp = arr[insert//2]
            arr[insert//2] = arr[insert]
            arr[insert] = tmp
            insert = insert//2
        else:
            break

    return arr

def min_heap_delete(arr):
    result = arr[1]
    arr[1] = arr[-1]
    arr.pop()
    delete = 1
    length = len(arr)-1

    while length >= delete * 2:
        if length == delete * 2:
            if arr[delete*2] < arr[delete]:
                tmp = arr[delete*2]
                arr[delete*2] = arr[delete]
                arr[delete] = tmp
                delete = delete*2
            else:
                break
        else:
            if arr[delete*2] < arr[delete*2 + 1]:
                if arr[delete*2] < arr[delete]:
                    tmp = arr[delete*2]
                    arr[delete*2] = arr[delete]
                    arr[delete] = tmp
                    delete = delete*2
                else:
                    break
            else:
                if arr[delete*2 +1] < arr[delete]:
                    tmp = arr[delete*2 + 1]
                    arr[delete*2 + 1] = arr[delete]
                    arr[delete] = tmp
                    delete = delete*2 +1
                else:
                    break
    return arr, result


for _ in range(n):
    temp = int(input())

    # max heap을 양수와 음수로 구분하여 구현
    if temp < 0:
        temp = abs(temp)
        minus_heap = min_heap_insert(minus_heap, temp)
        print(minus_heap)

    elif temp > 0:
        plus_heap = min_heap_insert(plus_heap, temp)
        print(plus_heap)

    # input 값이 0 일 때 각 heap의 마지막 값 출력
    elif temp == 0:
        if len(plus_heap) == 1 and len(minus_heap) == 1:
            string += '0\n'

        elif len(plus_heap) == 1:
            minus_heap, temp_string = min_heap_delete(minus_heap)
            string += str(-1 * temp_string) + '\n'
        elif len(minus_heap) == 1:
            plus_heap, temp_string = min_heap_delete(plus_heap)
            string += str(temp_string) + '\n'

        elif plus_heap[1] >= minus_heap[1]:
            minus_heap, temp_string = min_heap_delete(minus_heap)
            string += str(-1 * temp_string) + '\n'
        elif plus_heap[1] < minus_heap[1]:
            plus_heap, temp_string = min_heap_delete(plus_heap)
            string += str(temp_string) + '\n'

print(string)

# 내장 힙을 이용하여 구현

# 문제 14 solution
# 우선순위 큐를 이용하여 구현
from queue import PriorityQueue
import sys

print = sys.stdout.write
input = sys.stdin.readline

N = int(input())
myQueue = PriorityQueue()

for i in range(N):
    request = int(input())

    if request == 0:
        if myQueue.empty():
            print('0\n')
        else:
            temp = myQueue.get()
            print(str((temp[1]))+'\n')
    
    else:
        myQueue.put((abs(request), request))
