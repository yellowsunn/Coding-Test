# https://www.acmicpc.net/problem/11438

import math
import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(node, parent, depth):
    visited[node] = True
    parents[0][node] = parent
    depths[node] = depth
    for v in graph[node]:
        if not visited[v]:
            dfs(v, node, depth + 1)


def set_parents():
    for i in range(1, max_depth + 1):
        for j in range(1, n + 1):
            parents[i][j] = parents[i - 1][parents[i - 1][j]]


def find_lca(n1, n2):
    if depths[n1] > depths[n2]:
        n1, n2 = n2, n1

    for k in range(max_depth, -1, -1):
        if math.pow(2, k) <= depths[n2] - depths[n1]:
            n2 = parents[k][n2]

    for k in range(max_depth, -1, -1):
        if n1 == n2:
            break
        if parents[k][n1] != parents[k][n2]:
            n1 = parents[k][n1]
            n2 = parents[k][n2]
    lca = n1
    if n1 != n2:
        lca = parents[0][lca]
    return lca


n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
max_depth = math.floor(math.log2(n))
parents = [[0 for _ in range(n + 1)] for _ in range(max_depth + 1)]
depths = [0] * (n + 1)

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1, 0, 1)
set_parents()

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    print(find_lca(a, b))
