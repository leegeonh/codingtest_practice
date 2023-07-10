# 문제 25 : 친구관계 파악하기(DFS)

n, e = map(int, input().split())

node = [[] for _ in range(n)]

for _ in range(e):
    f, s = map(int, input().split())
    node[f].append(s)
    node[s].append(f)

load = [False] * n
t_f = False

def DFS(num, count):
    global t_f
    for i in node[num]:
        if load[i] == False:
            load[i] = True
            count += 1

            if count == 5:
                t_f = True
                break

            DFS(i, count)
        else:
            continue

    load[num] = False
    count -= 1

for i in range(n):
    if t_f is True:
        break

    load = [False] * n
    load[i] = True
    DFS(i, 1)

if t_f is False:
    print(0)
else:
    print(1)


# 문제 25 solution

import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().spilt())
arrive = False
a = [[] for _ in range(n+1)]
visited = [False] * (n+1)

def DFS(now, depth):
    global arrive

    if depth == 5:
        arrive = True
        return

    visited[now] = True

    for i in a[now]:
        if not visited[i]:
            DFS(i, depth+1)

    visited[now] = False

for _ in range(m):
    s, e = map(int, input().split())
    a[s].append(e)
    a[e].append(s)

for i in range(n):
    DFS(i, 1)
    if arrive:
        break

if arrive:
    print(1)
else:
    print(0)
