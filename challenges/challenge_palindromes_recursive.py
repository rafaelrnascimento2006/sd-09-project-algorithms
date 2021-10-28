def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if word == '' or word[int(low_index)] != word[int(high_index)]:
        return False
    elif high_index == 0:
        return True
    else:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
