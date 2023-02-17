# https://www.acmicpc.net/problem/1167

import sys
from collections import deque

input = sys.stdin.readline
v = int(input())
graph = [[] for _ in range(v + 1)]
for i in range(v):
    command = list(map(int, input().split()))
    for j in range(1, len(command), 2):
        if command[j] == -1:
            break
        graph[command[0]].append((command[j], command[j + 1]))


def bfs(start):
    q = deque()
    q.append((start, 0))
    distance = []
    visited = [False] * (v + 1)
    visited[start] = True
    while q:
        virtex = q.popleft()
        distance.append(virtex)
        for node in graph[virtex[0]]:
            if not visited[node[0]]:
                next_distance = virtex[1] + node[1]
                q.append((node[0], next_distance))
                visited[node[0]] = True

    distance.sort(key=lambda x: x[1], reverse=True)
    return distance[0]


result = bfs(1)
result = bfs(result[0])
print(result[1])
