# https://www.acmicpc.net/problem/1707

import sys
from collections import deque


def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1
    while q:
        pop = q.popleft()
        next_num = 2 if visited[pop] == 1 else 1
        for node in graph[pop]:
            if visited[node] == 0:
                q.append(node)
                visited[node] = next_num
            elif visited[pop] == visited[node]:
                return False
    return True


input = sys.stdin.readline
print = sys.stdout.write
k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    visited = [0] * (v + 1)
    is_success = True
    for i in range(1, v + 1):
        if visited[i] == 0:
            is_success = is_success and bfs(i)
        if not is_success:
            break
    print("YES\n" if is_success else "NO\n")
