def find_duplicate(nums: list) -> list:
    if isinstance(nums, list):
        for num in nums:
            if str(num).isalpha() or num < 0:
                break
            elif nums.count(num) > 1:
                return num
    return False
