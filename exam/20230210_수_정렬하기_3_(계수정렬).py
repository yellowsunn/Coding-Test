import sys

input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
counts = [0] * 10001

for _ in range(n):
    counts[int(input())] += 1

for i in range(10001):
    for j in range(counts[i]):
        print(f'{i}\n')
