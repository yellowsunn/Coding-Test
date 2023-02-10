# https://www.acmicpc.net/problem/6549
# 분할 정복

import sys

input = sys.stdin.readline
print = sys.stdout.write


def find_max_area(arr, start, end):
    if start == end:
        return arr[start]
    elif start > end:
        return 0
    mid = start + (end - start) // 2

    left_area = find_max_area(arr, start, mid)
    right_area = find_max_area(arr, mid + 1, end)

    ptr = mid + 1 if arr[mid] <= arr[mid + 1] else mid
    left_ptr, right_ptr = ptr - 1, ptr + 1
    height = arr[ptr]
    mid_area = arr[ptr]
    while left_ptr >= start and right_ptr <= end:
        if arr[left_ptr] <= arr[right_ptr]:
            height = min(height, arr[right_ptr])
            mid_area = max((right_ptr - left_ptr) * height, mid_area)
            right_ptr += 1
        else:
            height = min(height, arr[left_ptr])
            mid_area = max((right_ptr - left_ptr) * height, mid_area)
            left_ptr -= 1

    while left_ptr >= start:
        height = min(height, arr[left_ptr])
        mid_area = max((right_ptr - left_ptr) * height, mid_area)
        left_ptr -= 1
    while right_ptr <= end:
        height = min(height, arr[right_ptr])
        mid_area = max((right_ptr - left_ptr) * height, mid_area)
        right_ptr += 1

    return max(left_area, right_area, mid_area)


while True:
    input_str = input().rstrip()
    if input_str == '0':
        break
    histo = list(map(int, input_str.split()))
    result = find_max_area(histo, 1, len(histo) - 1)
    print(f'{result}\n')
