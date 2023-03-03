# https://www.acmicpc.net/problem/1325

import sys
from collections import deque

input = sys.stdin.readline
print = sys.stdout.write
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[b].append(a)


def bfs(start):
    q = deque()
    visited = [False] * (n + 1)
    q.append(start)
    visited[start] = True

    total_count = 0
    while q:
        node = q.popleft()
        total_count += 1
        for v in graph[node]:
            if not visited[v]:
                q.append(v)
                visited[v] = True
    return total_count


counts = []
for i in range(1, n + 1):
    counts.append((-bfs(i), i))
counts.sort()

for i in range(n):
    if counts[0][0] == counts[i][0]:
        print(f'{counts[i][1]} ')
    else:
        break
