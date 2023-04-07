# https://www.acmicpc.net/problem/2042

import math
import sys

input = sys.stdin.readline


def set_tree(i):
    while i != 1:
        tree[i // 2] += tree[i]
        i -= 1


def change_val(idx, val):
    idx = start + idx - 1
    tree[idx] = val
    while idx != 1:
        idx = idx // 2
        tree[idx] = tree[idx * 2] + tree[idx * 2 + 1]


def get_sum(start_idx, end_idx):
    start_idx = start_idx + start - 1
    end_idx = end_idx + start - 1
    total = 0
    while start_idx <= end_idx:
        if start_idx % 2 == 1:
            total += tree[start_idx]
        if end_idx % 2 == 0:
            total += tree[end_idx]
        start_idx = (start_idx + 1) // 2
        end_idx = (end_idx - 1) // 2
    return total


n, m, k = map(int, input().split())
start = int(math.pow(2, math.ceil(math.log2(n))))
size = start * 2

tree = [0] * size
for i in range(n):
    num = int(input())
    tree[start + i] = num
set_tree(size - 1)

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        change_val(b, c)
    else:
        print(get_sum(b, c))
