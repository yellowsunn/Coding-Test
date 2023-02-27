# https://www.acmicpc.net/problem/1033
# 유클리드 호제법 - 다시 풀만한 문제

import sys


def gcd(num1, num2):
    t1, t2 = sorted([num1, num2], reverse=True)
    while t1 % t2 > 0:
        t1, t2 = t2, t1 % t2
    return t2


def dfs(start, val):
    result[start] = val
    visited[start] = True
    for t in graph[start]:
        node = t[0]
        if visited[node]:
            continue
        dfs(node, result[start] // t[1] * t[2])


input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n)]
visited = [False] * n
result = [1] * n
lcm = 1
for _ in range(n - 1):
    a, b, p, q = map(int, input().split())
    graph[a].append((b, p, q))
    graph[b].append((a, q, p))
    lcm *= p * q // gcd(p, q)
dfs(0, lcm)

result_gcd = result[0]
for i in range(n - 1):
    result_gcd = gcd(result_gcd, result[i + 1])

for i in range(n):
    print(result[i] // result_gcd, end=' ')
