"""
source quicksort:
https://realpython.com/sorting-algorithms-python/
"""

from random import randint


def list_sort(list):
    if len(list) < 2:
        return list

    low = []
    same = []
    high = []

    pivot = list[randint(0, len(list) - 1)]

    for item in list:
        if item < pivot:
            low.append(item)
        elif item == pivot:
            same.append(item)
        else:
            high.append(item)

    return list_sort(low) + same + list_sort(high)


def is_anagram(first_string, second_string):
    first_list = list(first_string)
    second_list = list(second_string)
    return list_sort(first_list) == list_sort(second_list)
