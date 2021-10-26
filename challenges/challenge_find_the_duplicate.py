from challenges.merge_sort import merge_sort


def find_duplicate(nums):
    # 'or type(nums) == str' não precisou
    if not nums or len(nums) == 1:
        return False

    sorted_nums = merge_sort(nums)

    for index in range(len(sorted_nums) - 1):
        if type(sorted_nums[index]) == str or sorted_nums[index] < 0:
            return False
        elif sorted_nums[index] == sorted_nums[index + 1]:
            return sorted_nums[index]

    return False
