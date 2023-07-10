# 문제 26 : DFS / BFS
from collections import  deque
import sys
input = sys.stdin.readline

n, e, s = map(int,input().split())
node = [[] for _ in range(n+1)]

for _ in range(e):
    o, t = map(int, input().split())

    node[o].append(t)
    node[t].append(o)


depth_search = [0]
load = [False] * (n+1)
load[0] = True

def DFS(s):


    return depth_search

def BFS(arr):
    breadth_search = [0]
    load = [False] * (n+1)
    load[0] = True

    myqueue = deque()
    myqueue.append(s)

    while sum(load) != (n+1):
        tmp = myqueue.popleft()
        load[tmp] = True
        breadth_search.append(tmp)
        myqueue.extend(node[tmp])

    return breadth_search

print(DFS(node)[1:])
print(BFS(node)[1:])