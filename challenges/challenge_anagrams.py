from collections import Counter


# https://docs.python.org/3/library/collections.html#collections.Counter


def is_anagram(first_string, second_string):
    return Counter(first_string) == Counter(second_string)
