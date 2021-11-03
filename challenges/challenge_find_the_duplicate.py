def count_elements(element, nums):
    count = 0
    for num in nums:
        if num == element:
            count += 1
    return count


def find_duplicate(nums):
    for num in nums:
        if type(num) == str:
            return False
        if num < 0:
            return False
        if count_elements(num, nums) > 1:
            return num
    return False
