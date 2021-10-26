def find_duplicate(nums):
    """ Faça o código aqui. """
    for first_index, value in enumerate(nums):
        for second_index, element in enumerate(nums):
            if not str(element).isdigit() or element < 0:
                return False
            if element == value and first_index != second_index:
                return element
    return False
