import math
import sys

sys.setrecursionlimit(10 ** 6)
print = sys.stdout.write
n = int(input())


def is_prime_number(num):
    if num == 1:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


def dfs(num, num_range):
    if num_range == 0:
        print(f'{num}\n')
        return

    for i in range(1, 10):
        new_num = num * 10 + i
        if is_prime_number(new_num):
            dfs(new_num, num_range - 1)


dfs(0, n)
