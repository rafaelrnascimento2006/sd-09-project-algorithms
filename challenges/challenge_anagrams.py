def sort_string(word):
    string = list(word)
    if len(string) <= 1:
        return string
    mid = len(string) // 2
    left, right = sort_string(string[:mid]), sort_string(string[mid:])

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


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    string1 = sort_string(first_string)
    string2 = sort_string(second_string)

    if string1 == string2:
        return True
    return False


print(is_anagram('ovo', 'vos'))