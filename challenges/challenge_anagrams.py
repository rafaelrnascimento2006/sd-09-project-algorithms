def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if (first_string or second_string) in (None, ''):
        return False
    else:
        return sorted(first_string) == sorted(second_string)

print(is_anagram('', 'a'))