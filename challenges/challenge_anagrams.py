def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if len(first_string) != len(second_string):
        return False

    for i in first_string:
        if first_string.count(i) != second_string.count(i):
            return False

    return True
