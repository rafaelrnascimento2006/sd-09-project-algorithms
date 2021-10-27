def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if (first_string or second_string) in (None, ''):
        return False
    else:
        return sorted(first_string) == sorted(second_string)
     # se não explicitar que o sort() n pode ser usado eu n vejo rsrs
