def find_duplicate(nums):
    if not nums or len(nums) == 1:
        return False

    for index_one, number in enumerate(nums):
        if type(number) == str or number < 0:
            return False

        for index_two in range(index_one + 1, len(nums)):
            if nums[index_one] == nums[index_two]:
                return nums[index_two]

    return False
