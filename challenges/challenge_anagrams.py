# https://www.youtube.com/watch?v=fBk8BtSQQoA
# https://pymotw.com/2/collections/counter.html

import collections


def is_anagram(first_string, second_string):
    if first_string and second_string == '':
        return False

    if len(first_string) != len(second_string):
        return False

    first = collections.Counter(list(first_string))
    second = collections.Counter(list(second_string))
    return first == second
