import heapq
import sys

input = sys.stdin.readline
INF = 10 ** 9
v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(v + 1)]
distances = [INF] * (v + 1)
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))


def dijkstra(start):
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


dijkstra(k)
for i in range(1, v + 1):
    print(distances[i] if distances[i] < INF else "INF")
