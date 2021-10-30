# https://stackoverflow.com/questions/1185388/merge-sort-implementation-to-sort-by-string-length-python
# https://qastack.com.br/programming/1592649/examples-of-algorithms-which-has-o1-on-log-n-and-olog-n-complexities
def merge(left, right):
    ordered_chars = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            ordered_chars.append(left[i])
            i = i + 1
        else:
            ordered_chars.append(right[j])
            j = j + 1

    ordered_chars += left[i:]
    ordered_chars += right[j:]
    return ordered_chars


def merge_sort(string):
    if len(string) < 2:
        return string
    else:
        middle = len(string) // 2
        left = merge_sort(string[:middle])
        right = merge_sort(string[middle:])
        return merge(left, right)


def is_anagram(first_string, second_string):
    if len(first_string) != len(second_string):
        return False

    ordered_first_str = "".join(merge_sort(first_string.lower()))
    ordered_second_str = "".join(merge_sort(second_string.lower()))

    if ordered_first_str != ordered_second_str:
        return False

    return True
