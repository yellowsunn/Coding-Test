import math

a, b = map(int, input().split())
limit = int(math.sqrt(b))
is_primes = [True] * (limit + 1)
is_primes[1] = False
for i in range(2, int(math.sqrt(limit)) + 1):
    if not is_primes[i]:
        continue
    j = 2
    while i * j <= limit:
        is_primes[i * j] = False
        j += 1

count = 0
for i in range(2, limit + 1):
    if not is_primes[i]:
        continue
    j = 2
    while i ** j <= b:
        if i ** j >= a:
            count += 1
        j += 1
print(count)
