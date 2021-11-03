def find_duplicate(nums):
    if not nums or len(nums) < 1:
        return False
    for num in nums:
        if num < 0 or type(num) != int:
            return False
        if nums.count(num) > 1:
            return num
    return False
