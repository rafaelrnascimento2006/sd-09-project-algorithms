def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    try:
        if (
            low_index == high_index
            or low_index == high_index - 1
            and word[low_index] == word[high_index]
        ):
            return True
        elif word[low_index] == word[high_index]:
            return is_palindrome_recursive(word, low_index + 1, high_index - 1)
        else:
            return False
    except (IndexError, AssertionError):
        return False


# word = "AGUA"
# print(is_palindrome_recursive(word, 0, len(word) - 1))
