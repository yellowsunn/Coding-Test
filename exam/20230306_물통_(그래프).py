# https://www.acmicpc.net/problem/2251

from collections import deque


def bfs(start):
    q = deque()
    visited = set()
    q.append(start)
    visited.add(tuple(start))
    result = set()
    while q:
        node = q.popleft()
        if node[0] == 0:
            result.add(node[2])
        for i in range(3):
            for j in range(3):
                if i == j:
                    continue
                next_node = list(node)
                if node[i] + node[j] > max_amounts[j]:
                    next_node[j] = max_amounts[j]
                    next_node[i] = node[i] + node[j] - max_amounts[j]
                else:
                    next_node[j] = node[i] + node[j]
                    next_node[i] = 0
                if tuple(next_node) not in visited:
                    q.append(next_node)
                    visited.add(tuple(next_node))
    return sorted(result)


a, b, c = map(int, input().split())
max_amounts = [a, b, c]

print(*bfs([0, 0, c]), sep=' ')
