# Requisito 04
def find_duplicate(nums):
    if len(nums) < 2:
        return False

    sorted_nums = sorted(nums)

    for index in range(len(sorted_nums) - 1):
        if type(sorted_nums[index]) == str or sorted_nums[index] < 1:
            return False

        if sorted_nums[index] == sorted_nums[index + 1]:
            return sorted_nums[index]

    return False
