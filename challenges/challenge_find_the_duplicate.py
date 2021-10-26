from challenges.merge_sort import merge_sort


def find_duplicate(nums):
    if not nums or len(nums) < 2 or len(nums) == 2 and not nums[0] == nums[1]:
        return False

    sorted_nums = merge_sort(nums)

    for index, element in enumerate(sorted_nums):
        if not isinstance(element, int) or element < 0:
            return False

        if element == sorted_nums[index + 1]:
            return element

    return False
