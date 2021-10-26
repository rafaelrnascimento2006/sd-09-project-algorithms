def find_duplicate(nums):

    for i in nums:
        if type(i) != int or i < 1:
            return False
        if nums.count(i) != 1:
            return i

    return False
