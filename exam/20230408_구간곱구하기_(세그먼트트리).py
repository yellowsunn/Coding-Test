# https://www.acmicpc.net/problem/11505

import math
import sys


def set_tree(i):
    while i != 1:
        tree[i // 2] *= tree[i]
        tree[i // 2] %= REMAIN
        i -= 1


def set_val(idx, val):
    idx += start - 1
    tree[idx] = val
    while idx != 1:
        parent = idx // 2
        tree[parent] = tree[parent * 2] * tree[parent * 2 + 1] % REMAIN
        idx = parent


def get_multiple(start_idx, end_idx):
    start_idx += start - 1
    end_idx += start - 1
    total = 1
    while start_idx <= end_idx:
        if start_idx % 2 == 1:
            total = total * tree[start_idx] % REMAIN
        if end_idx % 2 == 0:
            total = total * tree[end_idx] % REMAIN
        start_idx = (start_idx + 1) // 2
        end_idx = (end_idx - 1) // 2
    return total


input = sys.stdin.readline
REMAIN = 1_000_000_007

n, m, k = map(int, input().split())
start = int(math.pow(2, math.ceil(math.log2(n))))
size = start * 2
tree = [1] * size

for i in range(n):
    tree[start + i] = int(input())
set_tree(size - 1)

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        set_val(b, c)
    else:
        print(get_multiple(b, c))
