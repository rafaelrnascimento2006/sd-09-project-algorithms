def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if not (first_string or second_string):
        return False
    else:
        fslist = ''.join(sorted(first_string))
        stlist = ''.join(sorted(second_string))
        return fslist == stlist
