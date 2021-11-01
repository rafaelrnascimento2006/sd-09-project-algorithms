def merge(value, begin, middle, end):
    left = value[begin:middle]
    right = value[middle:end]

    index_left = 0
    index_right = 0

    for index in range(begin, end):
        if (index_left >= len(left)):
            value[index] = right[index_right]
            index_right += 1
        elif (index_right >= len(right)):
            value[index] = left[index_left]
            index_left += 1
        elif (left[index_left] < right[index_right]):
            value[index] = left[index_left]
            index_left += 1
        else:
            value[index] = right[index_right]
            index_right += 1

    return value


def sort(value_sort, begin=0, end=None):
    if (end is None):
        end = len(value_sort)

    if (end - begin > 1):
        middle = (end + begin) // 2
        sort(value_sort, begin, middle)
        sort(value_sort, middle, end)
        return merge(value_sort, begin, middle, end)


def is_anagram(first_string, second_string):
    """ Faça o código aqui.  """
    if (first_string == '' or second_string == ''):
        return False

    if (sort(list(first_string)) == sort(list(second_string))):
        return True

    return False
