# https://www.acmicpc.net/problem/18352

import heapq
import sys


def dijkstra(start):
    q = []
    d[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        dist, node = heapq.heappop(q)
        if d[node] < dist:
            continue

        for v in graph[node]:
            next_dist = dist + 1
            if d[v] > next_dist:
                heapq.heappush(q, (next_dist, v))
                d[v] = next_dist
    return


INF = 10 ** 9
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
d = [INF for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
dijkstra(x)

result = ''
for i in range(1, n + 1):
    if d[i] == k:
        result += f'{i}\n'

print(result if result != '' else '-1\n')
