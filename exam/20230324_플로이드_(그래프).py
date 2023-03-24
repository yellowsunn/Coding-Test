# https://www.acmicpc.net/problem/11404

import sys

input = sys.stdin.readline
INF = 10 ** 9

n = int(input())
m = int(input())

graph = [[INF for _ in range(n + 1)] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a][b] = min(graph[a][b], c)

for i in range(1, n + 1):
    graph[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(graph[i][j] if graph[i][j] < INF else 0, end=' ')
    print()
