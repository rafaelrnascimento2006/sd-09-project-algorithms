def find_duplicate(nums):
    """ Faça o código aqui. """
    list_size = len(nums)
    is_valid_size = list_size > 1

    if not is_valid_size:
        return is_valid_size

    existing_numbers = []

    for number in nums:
        is_item_valid = type(number) == int and number >= 0

        if not is_item_valid:
            return is_item_valid

        is_duplicated = number in existing_numbers

        if is_duplicated:
            return number
        else:
            existing_numbers.append(number)

    return False
