def is_anagram(first_string, second_string):
    if(not first_string) or (not second_string):
        return False

    sorted_first_string = merge_sort(list(first_string))
    sorted_second_string = merge_sort(list(second_string))

    if(sorted_first_string != sorted_second_string):
        return False
    
    return True


#Referência: Course
def merge_sort(string):
    if len(string) <= 1:
        return string

    mid = len(string) // 2

    left, right = merge_sort(string[:mid]), merge_sort(string[mid:])

    return merge(left, right, string.copy())


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