def find_duplicate(nums):
    if len(nums) < 2:
        return False
    for num in nums:
        if not isinstance(num, int) or num < 0:
            return False
        if nums.count(num) > 1:
            return num
    return False
