# 문제 23 : 연결요소의 개수 구하기 (DFS)
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

node = [[] for _ in range(n+1)]
# edge = [[0]] * n+1

# 노드별 엣지
for i in range(m):
    u, v = map(int, input().split())

    if i == 0:
        start_point = u

    node[u].append(v)
    node[v].append(u)

count = 1
load = [False for _ in range(n+1)]
load[0] = True
stack = [start_point]

while not all(load):
    if stack:
        pop = stack.pop()

        for input in node[pop]:
            if load[input] == False:
                stack.append(input)
                load[input] = True

    else:
        count += 1
        for i in range(len(load)):
            if load[i] == False:
                stack.append(i)
                load[i] == True

print(count)


# 문제 23 solution

sys.setrecursionlimit(10000) # 제귀함수 호출시 필수적으로 호출할 것

n, m = map(int, input().split())
A = [[] for _ in range(n+1)]
visited = [False] * (n+1)

def DFS(v):
    visited[v] = True

    for i in A[v]:
        if not visited[i]:
            DFS(i)

for _ in range(m):
    s, e = map(int, input().split())
    A[s].append(e)
    A[e].append(s)

count = 0



for i in range(1, n+1):
    if not visited[i]:
        count += 1
        DFS(i)

print(count)
