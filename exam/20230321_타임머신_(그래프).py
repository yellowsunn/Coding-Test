# https://www.acmicpc.net/problem/11657

import sys

input = sys.stdin.readline
INF = 10 ** 9

n, m = map(int, input().split())
edges = []
d = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))


def bellman(start):
    d[start] = 0
    for _ in range(n - 1):
        for a, b, c in edges:
            if d[a] == INF:
                continue
            if d[b] > d[a] + c:
                d[b] = d[a] + c

    for a, b, c in edges:
        if d[a] == INF:
            continue
        if d[b] > d[a] + c:
            return False

    return True


has_not_circle = bellman(1)
if has_not_circle:
    for i in range(2, n + 1):
        print(d[i] if d[i] < INF else -1)
else:
    print(-1)
