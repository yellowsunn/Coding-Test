# https://www.acmicpc.net/problem/11047

import sys

input = sys.stdin.readline
n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

count = 0
idx = n - 1
while k != 0:
    share = k // coins[idx]
    if share > 0:
        k -= share * coins[idx]
        count += share
    else:
        idx -= 1
print(count)
