# https://www.acmicpc.net/problem/1948

import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


# dp
def calculate_distance(s):
    if distances[s] != 0:
        return distances[s]

    max_distance = 0
    for v, dist in graph[s]:
        max_distance = max(max_distance, calculate_distance(v) + dist)
    distances[s] = max_distance
    return distances[s]


def count_road(s):
    q = deque()
    q.append(s)
    count = 0
    visited = set()
    while q:
        node = q.popleft()
        for v, dist in graph[node]:
            if (node, v) in visited:
                continue
            if distances[v] == distances[node] - dist:
                q.append(v)
                visited.add((node, v))
                count += 1
    return count


n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
distances = [0] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[b].append((a, c))

start, end = map(int, input().split())

calculate_distance(end)
print(distances[end])
print(count_road(end))
