def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if high_index < 0:
        return False

    if len(word) < 2:
        return True
    else:
        if word[0] == word[-1]:
            return is_palindrome_recursive(word[1:-1], low_index, high_index - 1)
        else:
            return False
