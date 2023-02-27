# https://www.acmicpc.net/problem/11689

import math

n = int(input())

result = n
for i in range(2, int(math.sqrt(n)) + 1):
    print(i)
    if n % i == 0:
        result -= result // i
        while n % i == 0:
            n //= i

if n > 1:
    result -= result // n
print(result)