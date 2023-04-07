# https://www.acmicpc.net/problem/1068

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


def dfs(start):
    global total_leaf_node
    visited[start] = True

    child_count = 0
    for node in graph[start]:
        if not visited[node] and node != remove_node:
            dfs(node)
            child_count += 1

    if child_count == 0:
        total_leaf_node += 1


n = int(input())
parents = list(map(int, input().split()))
remove_node = int(input())
graph = [[] for _ in range(n)]
visited = [False] * n
root = 0
total_leaf_node = 0

for i in range(n):
    if parents[i] == -1:
        root = i
        continue
    graph[parents[i]].append(i)

if root == remove_node:
    print(0)
else:
    dfs(root)
    print(total_leaf_node)
