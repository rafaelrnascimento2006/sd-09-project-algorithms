def is_anagram(first_string, second_string):
    first_string_list = list(first_string)
    second_string_list = list(second_string)

    if (not len(first_string) or not len(second_string)):
        return False

    first_string_test = sort_string(first_string_list)
    second_string_test = sort_string(second_string_list)

    if (first_string_test != second_string_test):
        return False

    if first_string_test == second_string_test:
        return True


def sort_string(array_string):
    if len(array_string) <= 1:
        return array_string

    mid = len(array_string) // 2

    left, right = sort_string(array_string[:mid]), sort_string(
        array_string[mid:]
    )

    return merge(left, right, array_string.copy())


def merge(left, right, merged):

    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged[left_cursor + right_cursor] = left[left_cursor]

    # itera sobre os elementos restantes na partição "direita"
    # inserindo-os no array de mistura
    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged
