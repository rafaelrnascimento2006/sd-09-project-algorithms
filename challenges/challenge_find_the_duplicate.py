def find_duplicate(nums):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if not isinstance(nums[j], int) or nums[j] < 0:
                return False
            elif nums[j] == nums[i]:
                return nums[j]
    return False