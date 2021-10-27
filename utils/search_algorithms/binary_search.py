def binary_search(array, low_index, high_index, value):
    if high_index < low_index:
        raise ValueError(f"{value} is not in list")

    middle_index = (high_index + low_index) // 2

    if array[middle_index] == value:
        return middle_index
    elif array[middle_index] > value:
        return binary_search(array, low_index, middle_index - 1, value)
    else:
        return binary_search(array, middle_index + 1, high_index, value)