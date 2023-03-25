n = int(input())
nums = list(map(int, input().split()))
d = [[-1 for _ in range(21)] for _ in range(101)]


def dp(end_idx, total):
    if end_idx == 0:
        return 1 if total == nums[end_idx] else 0
    if d[end_idx][total] != -1:
        return d[end_idx][total]

    count = 0
    if 0 <= total - nums[end_idx] <= 20:
        count += dp(end_idx - 1, total - nums[end_idx])
    if 0 <= total + nums[end_idx] <= 20:
        count += dp(end_idx - 1, total + nums[end_idx])
    d[end_idx][total] = count
    return count


result = dp(n - 2, nums[n - 1])
print(result)
