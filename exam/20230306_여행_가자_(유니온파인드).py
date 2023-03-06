# https://www.acmicpc.net/problem/1976

import sys

input = sys.stdin.readline


def find_parent(x):
    if x == parent[x]:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]


def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a <= b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
m = int(input())
graph = []
parent = [i for i in range(n + 1)]

for i in range(n):
    graph.append(list(map(int, input().split())))
plans = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        if graph[i][j] == 0 or i == j:
            continue
        union(i + 1, j + 1)

plan_parent = find_parent(plans[0])
is_same = True
for i in range(m):
    if plan_parent != find_parent(plans[i]):
        is_same = False
        break
print("YES" if is_same else "NO")
