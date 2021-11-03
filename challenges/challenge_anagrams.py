from challenges.utils.merge_sort import merge_sort


def order_string(string):
    return ''.join(merge_sort([char for char in string]))


def is_anagram(first_string, second_string):
    """ Faça o código aqui... """

    if not first_string or not second_string:
        return False

    ordered_first_string = order_string(first_string)
    ordered_second_string = order_string(second_string)
    return ordered_first_string == ordered_second_string
