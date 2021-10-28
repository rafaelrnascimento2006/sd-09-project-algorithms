def merge_sort(list):
    if len(list) <= 1:
        return list

    mid = len(list) // 2
    left, right = merge_sort(list[:mid]), merge_sort(list[mid:])
    return merge(left, right, list.copy())

def merge(left, right, list_merged):
    left_cursor, right_cursor = 0, 0
    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            list_merged[left_cursor + right_cursor] = left[left_cursor]
            left_cursor += 1
        else:
            list_merged[left_cursor + right_cursor] = right[right_cursor]
            right_cursor += 1
            
    for left_cursor in range(left_cursor, len(left)):
            list_merged[left_cursor + right_cursor] = left[left_cursor]
    
    for right_cursor in range(right_cursor, len(right)):
            list_merged[left_cursor + right_cursor] = right[right_cursor]
    return list_merged


def is_anagram(first_string, second_string):
    first = [item for item in first_string]
    second = [item for item in second_string]

    if merge_sort(first) == merge_sort(second):
        return True
    return False


print(is_anagram('bolas', 'lobo'))
