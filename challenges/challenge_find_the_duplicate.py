def find_duplicate(nums):
    if len(nums) < 2:
        return False
    try:
        return find_duplicate_algorithm(nums)
    except ValueError:
        return False


def find_duplicate_algorithm(nums):
    for i in range(len(nums)):
        if int(nums[i]) < 0:
            return False
        for j in range(len(nums[slice(i)])):
            if nums[i] == nums[j]:
                return nums[i]
    return False
