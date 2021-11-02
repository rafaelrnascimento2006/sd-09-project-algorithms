def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if not first_string or not second_string:
        return False

    if len(first_string) == len(second_string):
        first = first_string.split('')
        second = second_string.split('')

        if first.sort() == second.sort():
            return True

    return False
