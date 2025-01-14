def two_sum(nums, target):
    num_map = {}

    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i


nums = [3, 7, 11, 6]
target = 9
result = two_sum(nums, target)
print(result)
