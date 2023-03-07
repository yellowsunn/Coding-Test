# https://www.acmicpc.net/problem/1516

import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
graph = [[] for _ in range(n + 1)]
times = [0] * (n + 1)
d = [0] * (n + 1)
for i in range(n):
    nums = list(map(int, input().split()))[:-1]
    times[i + 1] = nums[0]
    for num in nums[1:]:
        graph[num].append(i + 1)
        d[i + 1] += 1


def topological_sort():
    q = deque()
    for i in range(1, n + 1):
        if d[i] == 0:
            q.append(i)

    total_times = [0] * (n + 1)
    while q:
        idx = q.popleft()
        total_times[idx] += times[idx]
        for v in graph[idx]:
            d[v] -= 1
            total_times[v] = max(total_times[v], total_times[idx])
            if d[v] <= 0:
                q.append(v)
    return total_times[1:]


result = topological_sort()
print(*result, sep='\n')
