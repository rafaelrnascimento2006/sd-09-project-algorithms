def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    try:
        if word[low_index] != word[high_index]:
            return False
        else:
            if low_index == high_index or low_index == high_index + 1:
                return True
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    except IndexError:
        return False