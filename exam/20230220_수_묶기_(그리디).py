# https://www.acmicpc.net/problem/1744

import heapq
import sys

input = sys.stdin.readline
n = int(input())

plus = []
minus = []
zeroCount = 0
oneCount = 0

total = 0
for _ in range(n):
    num = int(input())
    if num >= 2:
        heapq.heappush(plus, -num)
    elif num <= -1:
        heapq.heappush(minus, num)
    elif num == 0:
        zeroCount += 1
    else:  # num == 1
        oneCount += 1

while len(plus) >= 2:
    first = heapq.heappop(plus)
    second = heapq.heappop(plus)
    total += first * second

while len(minus) >= 2:
    first = heapq.heappop(minus)
    second = heapq.heappop(minus)
    total += first * second

while zeroCount > 0 and minus:
    heapq.heappop(minus)
    zeroCount -= 1

while plus:
    total += -heapq.heappop(plus)

while minus:
    total += heapq.heappop(minus)

total += oneCount
print(total)
