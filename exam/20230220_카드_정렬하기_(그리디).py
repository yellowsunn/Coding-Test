# https://www.acmicpc.net/problem/1715

import heapq
import sys

input = sys.stdin.readline
n = int(input())
nums = []
for _ in range(n):
    heapq.heappush(nums, int(input()))

total_count = 0
while len(nums) >= 2:
    first = heapq.heappop(nums)
    second = heapq.heappop(nums)
    count = first + second
    heapq.heappush(nums, count)
    total_count += count
print(total_count)
