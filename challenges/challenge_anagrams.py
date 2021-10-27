from challenges.merge_sort import merge_sort


def is_anagram(first_string, second_string):
    return merge_sort(list(first_string)) == merge_sort(list(second_string))
