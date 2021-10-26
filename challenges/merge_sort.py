def merge_sort(word):

    if len(word) <= 1:
        return word

    mid = len(word) // 2

    left, right = merge_sort(word[:mid]), merge_sort(word[mid:])

    return merge(left, right, list(word))


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

    for right_cursor in range(right_cursor, len(right)):
        merged[left_cursor + right_cursor] = right[right_cursor]

    return merged
