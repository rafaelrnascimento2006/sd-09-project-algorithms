from challenges.floyds_tortoise_and_hare import floyds_tortoise_and_hare


def find_duplicate(nums):
    if len(nums) < 2:
        return False
    try:
        if len(nums) == 2 and int(nums[0]) > 0:
            return nums[0] == nums[1]
        return floyds_tortoise_and_hare(nums)
    except ValueError:
        return False


def find_duplicate_algorithm(nums):
    for i in range(len(nums)):
        if nums[i] < 0:
            return False
        for j in range(len(nums)):
            if i != j and nums[i] == nums[j]:
                return nums[i]
    return False
