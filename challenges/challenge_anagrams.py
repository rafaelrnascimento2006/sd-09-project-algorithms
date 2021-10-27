def is_anagram(first_string, second_string):
    """"""
    if len(first_string) != len(second_string):
        return False
    first = quicksort(first_string)
    second = quicksort(second_string)
    if first != second:
        return False
    return True


def quicksort(string):
    if len(string) <= 1:
        return string

    min_string = string[string.index(min(string))]
    splitted = string.split(min_string)
    return (min_string * (len(splitted) - 1)) + quicksort(''.join(splitted))
