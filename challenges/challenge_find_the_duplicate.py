def find_duplicate(nums):
    """ Faça o código aqui. """
    list_size = len(nums)
    is_valid_size = list_size > 1

    if not is_valid_size:
        return is_valid_size

    for i in nums:
        if type(i) != int or i < 0:
            return False

    return 0
