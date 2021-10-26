def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if not (first_string or second_string):
        return False
    else:
        return sorted(first_string) == sorted(second_string)
