# https://www.acmicpc.net/problem/1717

import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
print = sys.stdout.write


def find_parent(x):
    if x == parent[x]:
        return x
    parent[x] = find_parent(parent[x])
    return parent[x]


def union(n1, n2):
    n1 = find_parent(n1)
    n2 = find_parent(n2)
    if n1 <= n2:
        parent[n2] = n1
    else:
        parent[n1] = n2


n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

for _ in range(m):
    x, a, b = map(int, input().split())
    if x == 0:
        union(a, b)
    else:
        print("YES\n" if find_parent(a) == find_parent(b) else "NO\n")
