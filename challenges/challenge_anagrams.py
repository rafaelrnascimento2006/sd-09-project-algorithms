from challenges.merge_sort import merge_sort

def is_anagram(first_string, second_string):
    if first_string and second_string == '':
        return False

    if len(first_string) != len(second_string):
        return False

    first_word = merge_sort(first_string)
    second_word = merge_sort(second_string)

    return first_word == second_word
