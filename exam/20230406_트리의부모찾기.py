import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(start, parent):
    visited[start] = True
    parents[start] = parent
    for node in graph[start]:
        if not visited[node]:
            dfs(node, start)


n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
parents = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1, 0)
for i in range(2, n + 1):
    print(parents[i])