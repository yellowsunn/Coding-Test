# https://www.acmicpc.net/problem/2252

import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write
n, m = map(int, input().split())
d = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    d[b] += 1


def topological_sort():
    q = deque()
    for i in range(1, n + 1):
        if d[i] == 0:
            q.append(i)
    while q:
        node = q.popleft()
        print(f'{node} ')
        for v in graph[node]:
            d[v] -= 1
            if d[v] <= 0:
                q.append(v)


topological_sort()
