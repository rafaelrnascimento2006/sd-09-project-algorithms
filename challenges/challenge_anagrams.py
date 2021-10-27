from collections import Counter


def is_anagram(first_string, second_string):
    return Counter(list(first_string)) == Counter(list(second_string))
