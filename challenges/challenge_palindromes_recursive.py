def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if len(word) - 1 == low_index:
        return True
    elif len(word) == 0 or word[low_index] != word[high_index]:
        return False

    return is_palindrome_recursive(word, low_index + 1, high_index - 1)
