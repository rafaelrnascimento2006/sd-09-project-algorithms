def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    if first_string == '' or second_string == '' or (
        len(first_string) != len(second_string)
    ):
        return False
    else:
        for i in range(len(first_string)):
            if len(first_string) > 0:
                second_string = second_string.replace(first_string[0], '')
                first_string = first_string.replace(first_string[0], '')
            if len(first_string) != len(second_string):
                return False
        return True
