import sys
from collections import deque


def dfs(start, visited):
    visited[start] = True
    print(f'{start} ')
    for node in graph[start]:
        if not visited[node]:
            dfs(node, visited)


def bfs(start, visited):
    q = deque()
    q.append(start)
    visited[start] = True
    while q:
        v = q.popleft()
        print(f'{v} ')
        for node in graph[v]:
            if not visited[node]:
                q.append(node)
                visited[node] = True


input = sys.stdin.readline
print = sys.stdout.write

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n + 1):
    graph[i].sort()

dfs(v, [False] * (n + 1))
print('\n')
bfs(v, [False] * (n + 1))
