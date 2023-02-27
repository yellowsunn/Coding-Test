# https://www.acmicpc.net/problem/1016

import math

min_num, max_num = map(int, input().split())

arr = [True] * (max_num - min_num + 1)

for i in range(2, int(math.sqrt(max_num)) + 1):
    num = i * i
    j = math.ceil(min_num / num)

    while num * j <= max_num:
        arr[num * j - min_num] = False
        j += 1

count = 0
for i in range(len(arr)):
    if arr[i]:
        count += 1
print(count)
