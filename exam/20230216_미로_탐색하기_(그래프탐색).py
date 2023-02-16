import sys
from collections import deque


def bfs(start):
    q = deque()
    q.append((*start, 1))
    graph[start[0]][start[1]] = 0
    while q:
        v = q.popleft()
        if v[0] == n - 1 and v[1] == m - 1:
            return v[2]
        for i in range(4):
            next_row = v[0] + move_row[i]
            next_col = v[1] + move_col[i]
            next_count = v[2] + 1
            if 0 <= next_row < n and 0 <= next_col < m and graph[next_row][next_col] == 1:
                q.append((next_row, next_col, next_count))
                graph[next_row][next_col] = 0
    return -1


input = sys.stdin.readline
n, m = map(int, input().split())
move_row = [0, -1, 0, 1]
move_col = [-1, 0, 1, 0]

graph = [[] for i in range(n)]
for i in range(n):
    read_str = input()
    for j in range(m):
        graph[i].append(int(read_str[j]))

result = bfs((0, 0))
print(result)
