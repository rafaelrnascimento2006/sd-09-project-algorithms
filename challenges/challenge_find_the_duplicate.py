from challenges.floyds_tortoise_and_hare import floyds_tortoise_and_hare


def find_duplicate(nums):
    if len(nums) < 2:
        return False
    try:
        if len(nums) == 2 and nums[0] != nums[1]:
            return False
        return floyds_tortoise_and_hare(nums)
    except ValueError:
        return False


def find_duplicate_algorithm(nums):
    for i in range(len(nums)):
        if int(nums[i]) < 0:
            return False
        for j in range(len(nums[:i])):
            if nums[i] == nums[j]:
                return nums[i]
    return False
