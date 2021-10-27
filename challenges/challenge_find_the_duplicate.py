def search_number(nums):
    ordered_array = sorted(nums)
    for index in range(len(ordered_array) - 1):
        if ordered_array[index] == ordered_array[index + 1]:
            return ordered_array[index]
    return False


def find_duplicate(nums):
    """ Faça o código aqui. """
    if len(nums) < 2:
        return False
    for number in nums:
        if not isinstance(number, int) or number < 0:
            return False
    return search_number(nums)
