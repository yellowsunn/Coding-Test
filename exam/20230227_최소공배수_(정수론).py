# https://www.acmicpc.net/problem/1934

import sys

input = sys.stdin.readline
print = sys.stdout.write
t = int(input())
for _ in range(t):
    a, b = sorted(map(int, input().split()), reverse=True)
    n1, n2 = a, b
    while n1 % n2 > 0:
        n1, n2 = n2, n1 % n2
    print(f'{n2 * a // n2 * b // n2}\n')
