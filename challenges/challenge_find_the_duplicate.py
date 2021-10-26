def find_duplicate(nums):
    if len(nums) <= 1 or type(nums) != list:
        return False
    ordened_nums = sorted(nums)
    for index in range(len(ordened_nums)):
        if (
            type(ordened_nums[index]) != int
            or ordened_nums[index] < 0
            or index >= len(ordened_nums) - 1
        ):
            return False
        if ordened_nums[index] == ordened_nums[index + 1]:
            return ordened_nums[index]
    return False
