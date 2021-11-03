def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    is_anagram = False

    if len(first_string) != len(second_string):
        return False

    for letter in first_string:
        if letter in second_string:
            is_anagram = True
        else:
            is_anagram = False
            break

        # https://stackoverflow.com/questions/1228299/changing-one-character-in-a-string
        letter_index = second_string.find(letter)
        second_string = (
            second_string[:letter_index] +
            '' + second_string[letter_index+1:])
    return is_anagram