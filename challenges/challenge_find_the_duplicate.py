def find_duplicate(nums):
    if len(nums) < 2:
        return False
    try:
        return find_duplicate_algorithm(nums)
    except TypeError:
        return False


def find_duplicate_algorithm(nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] < 0 or nums[j] < 0:
                return False
            if i != j and nums[i] == nums[j]:
                return nums[i]
    return False
