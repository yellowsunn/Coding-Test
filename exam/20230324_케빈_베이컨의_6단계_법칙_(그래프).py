# https://www.acmicpc.net/problem/1389

import sys

input = sys.stdin.readline
INF = 10 ** 9

n, m = map(int, input().split())
graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1
for i in range(1, n + 1):
    graph[i][i] = 0

for k in range(n + 1):
    for i in range(n + 1):
        for j in range(n + 1):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

result = []
for i in range(1, n + 1):
    result.append((sum(graph[i][1: n + 1]), i))
result.sort()

print(result[0][1])
