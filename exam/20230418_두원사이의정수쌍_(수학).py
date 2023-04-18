import math


def solution(r1, r2):
    count = r2 - r1 + 1
    for col in range(1, r2):
        count += find_max_row(col, r2) - find_min_row(col, r1) + 1
    return count * 4


def find_max_row(col, r2):
    return int(math.sqrt(r2 ** 2 - col ** 2))


def find_min_row(col, r1):
    if col >= r1:
        return 1
    return int(math.ceil(math.sqrt(r1 ** 2 - col ** 2)))
