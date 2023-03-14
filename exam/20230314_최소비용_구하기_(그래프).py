import heapq
import sys

input = sys.stdin.readline
INF = 10 ** 9

n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
s, e = map(int, input().split())


def dijkstra(start, end):
    distances = [INF] * (n + 1)
    q = []
    heapq.heappush(q, (0, start))
    distances[start] = 0
    while q:
        dist, idx = heapq.heappop(q)
        if dist > distances[idx]:
            continue

        for v_idx, v_dist in graph[idx]:
            next_dist = dist + v_dist
            if next_dist < distances[v_idx]:
                heapq.heappush(q, (next_dist, v_idx))
                distances[v_idx] = next_dist
    return distances[end]


print(dijkstra(s, e))
