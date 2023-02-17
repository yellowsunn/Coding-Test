n = int(input())
k = int(input())

start, end = 1, 10 ** 9
while start <= end:
    mid = start + (end - start) // 2
    count = 0
    for i in range(1, n + 1):
        count += min(mid // i, n)

    if count < k:
        start = mid + 1
    else:
        end = mid - 1
print(start)
