def find_duplicate(nums):

    if len(nums) < 2 or type(nums[0]) is str:
        return False

    if nums[0] < 0 or nums[1] < 0:
        return False

    nums.sort()

    for index in range(len(nums)-1):
        if nums[index + 1] == nums[index]:
            return nums[index]

    return False
