# https://www.acmicpc.net/problem/11724

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def dfs(start: int):
    visited[start] = True
    for node in graph[start]:
        if not visited[node]:
            dfs(node)


result = 0
for i in range(1, n + 1):
    if not visited[i]:
        result += 1
        dfs(i)
print(result)
