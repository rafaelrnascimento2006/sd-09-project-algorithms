def merge(first, second, merged):
    first_cursor, second_cursor = 0, 0

    while first_cursor < len(first) and second_cursor < len(second):
        if first[first_cursor] <= second[second_cursor]:
            merged[first_cursor + second_cursor] = first[first_cursor]
            first_cursor += 1
        else:
            merged[first_cursor + second_cursor] = second[second_cursor]
            second_cursor += 1

    for first_cursor in range(first_cursor, len(first)):
        merged[first_cursor + second_cursor] = first[first_cursor]

    for second_cursor in range(second_cursor, len(second)):
        merged[second_cursor + first_cursor] = second[second_cursor]

    return merged


def merge_sort(list: list) -> list:
    if len(list) == 1:
        return list
    mid = len(list) // 2
    first, second = merge_sort(list[:mid]), merge_sort(list[mid:])
    return merge(first, second, list.copy())


def is_anagram(first_string, second_string):
    if not first_string or not second_string:
        return False
    first_string = merge_sort(list(first_string))
    second_string = merge_sort(list(second_string))
    return first_string == second_string
