from challenges.merge_sort import merge_sort


def is_anagram(first_string, second_string):
    if not len(first_string) == len(second_string):
        return False

    sorted_first_string = merge_sort(first_string)
    sorted_second_string = merge_sort(second_string)

    return sorted_first_string == sorted_second_string
