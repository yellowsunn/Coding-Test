# https://www.acmicpc.net/problem/1854

import heapq
import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
d = [[1] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    heapq.heappush(d[start], 0)

    while q:
        dist, idx = heapq.heappop(q)

        for v_idx, v_dist in graph[idx]:
            next_dist = dist + v_dist

            heapq.heappush(d[v_idx], -next_dist)
            if len(d[v_idx]) > k + 1:
                max_dist = heapq.heappop(d[v_idx])
                if max_dist == -next_dist:
                    continue

            heapq.heappush(q, (next_dist, v_idx))


dijkstra(1)
for i in range(1, n + 1):
    if len(d[i]) < k + 1:
        print(-1)
        continue
    distance = heapq.heappop(d[i])
    print(-distance if distance != 1 else -1)
