def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    fslist = list(first_string.lower())
    stlist = list(second_string.lower())
    fslist.sort()
    stlist.sort()
    return fslist == stlist
