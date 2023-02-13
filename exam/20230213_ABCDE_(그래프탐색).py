import sys

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [False for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

result = 0


def dfs(start, depth):
    global result
    if result == 1:
        return
    if depth == 5:
        result = 1
        return

    visited[start] = True
    for node in graph[start]:
        if not visited[node]:
            dfs(node, depth + 1)

    visited[start] = False


for i in range(n):
    dfs(i, 1)
print(result)
