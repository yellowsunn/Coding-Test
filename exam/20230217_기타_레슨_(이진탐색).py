n, m = map(int, input().split())
nums = list(map(int, input().split()))

start, end = max(nums), sum(nums)
while start <= end:
    mid = start + (end - start) // 2
    blue_rays = [0]
    for i in range(n):
        length = blue_rays[-1] + nums[i]
        if length <= mid:
            blue_rays[-1] += nums[i]
        else:
            blue_rays.append(nums[i])
    if len(blue_rays) <= m:
        end = mid - 1
    else:
        start = mid + 1
print(start)
