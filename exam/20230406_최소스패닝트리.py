# https://www.acmicpc.net/problem/1197

import sys

input = sys.stdin.readline


def find_parent(x):
    if x == parents[x]:
        return x
    parents[x] = find_parent(parents[x])
    return parents[x]


def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a <= b:
        parents[b] = a
    else:
        parents[a] = b


v, e = map(int, input().split())
parents = [i for i in range(v + 1)]
edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))
edges.sort()

total_distance = 0
for edge in edges:
    distance, node_a, node_b = edge
    if find_parent(node_a) != find_parent(node_b):
        total_distance += distance
        union_parent(node_a, node_b)
print(total_distance)
