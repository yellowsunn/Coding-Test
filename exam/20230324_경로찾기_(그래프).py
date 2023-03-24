# https://www.acmicpc.net/problem/11403

import sys

input = sys.stdin.readline
INF = 10 ** 9

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(lambda x: int(x) if x != '0' else INF, input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][k] + graph[k][j], graph[i][j])

for i in range(n):
    for j in range(n):
        print(1 if graph[i][j] < INF else 0, end=' ')
    print()