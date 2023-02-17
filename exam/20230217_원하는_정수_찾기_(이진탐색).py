import bisect
import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
nums = sorted(map(int, input().split()))
m = int(input())
finds = list(map(int, input().split()))

for find in finds:
    idx = bisect.bisect_left(nums, find)
    if 0 <= idx < n and nums[idx] == find:
        print('1\n')
    else:
        print('0\n')
