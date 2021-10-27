def find_duplicate(list_of_nums):
    if len(list_of_nums) == 1:
        return False
    for index in range(len(list_of_nums) - 1):
        if isinstance(list_of_nums[index], str) or list_of_nums[index] < 0:
            return False
    return sort_and_find_duplicate(list_of_nums)


def sort_and_find_duplicate(nums):
    sorted_list = sorted(nums)
    for index in range(len(sorted_list) - 1):
        if sorted_list[index] == sorted_list[index + 1]:
            return sorted_list[index]
    return False
