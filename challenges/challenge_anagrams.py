def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False
    return merge_sort(first_string) == merge_sort(second_string)


def merge_sort(string):
    # algoritmo de merge sort adaptado do código mostrado no course
    # https://app.betrybe.com/course/computer-science/algoritmos/algoritmos-de-ordenacao-e-busca/29521083-44ea-488d-a74d-216b1ac79b04/conteudos/8697a14b-5092-4b17-b488-71a8b2ab315f/algoritmos-de-ordenacao/3905a5da-452f-450e-9874-056f1a693205?use_case=side_bar
    if len(string) <= 1:
        return string
    middle = len(string) // 2
    left, right = merge_sort(string[:middle]), merge_sort(string[middle:])
    return merge(left, right)


def merge(left, right):
    merged = ''
    left_cursor, right_cursor = 0, 0

    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] <= right[right_cursor]:
            merged += left[left_cursor]
            left_cursor += 1
        else:
            merged += right[right_cursor]
            right_cursor += 1

    for left_cursor in range(left_cursor, len(left)):
        merged += left[left_cursor]

    for right_cursor in range(right_cursor, len(right)):
        merged += right[right_cursor]

    return merged
