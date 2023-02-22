import math
import sys

print = sys.stdout.write

m, n = map(int, input().split())
is_primes = [True] * (n + 1)
is_primes[1] = False
for i in range(2, int(math.sqrt(n)) + 1):
    if not is_primes[i]:
        continue
    j = 2
    while i * j <= n:
        is_primes[i * j] = False
        j += 1

for i in range(m, n + 1):
    if is_primes[i]:
        print(f'{i}\n')
