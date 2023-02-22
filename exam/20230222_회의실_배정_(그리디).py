import sys

input = sys.stdin.readline
n = int(input())
ranges = []
for _ in range(n):
    start, end = map(int, input().split())
    ranges.append((start, end))

ranges.sort(key=lambda x: (x[1], x[0]))

prev_start, prev_end = 0, 0
count = 0

for r in ranges:
    start, end = r[0], r[1]
    if prev_end <= start:
        count += 1
        prev_start, prev_end = start, end
print(count)
