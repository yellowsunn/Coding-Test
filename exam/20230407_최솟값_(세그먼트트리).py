# https://www.acmicpc.net/problem/10868

import math
import sys

input = sys.stdin.readline
INF = 10 ** 9


def set_tree(i):
    while i != 1:
        parent = i // 2
        tree[parent] = min(tree[parent * 2], tree[parent * 2 + 1])
        i -= 1


def find_min(start_idx, end_idx):
    start_idx += start - 1
    end_idx += start - 1
    interval_min = INF
    while start_idx <= end_idx:
        if start_idx % 2 == 1:
            interval_min = min(tree[start_idx], interval_min)
        if end_idx % 2 == 0:
            interval_min = min(tree[end_idx], interval_min)
        start_idx = (start_idx + 1) // 2
        end_idx = (end_idx - 1) // 2
    return interval_min


n, m = map(int, input().split())
start = int(math.pow(2, math.ceil(math.log2(n))))
size = start * 2
tree = [INF] * size

for i in range(n):
    tree[start + i] = int(input())
set_tree(size - 1)

for _ in range(m):
    a, b = map(int, input().split())
    print(find_min(a, b))
