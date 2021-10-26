def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if not word:
        return False

    if len(word) <= 1:
        return True

    if word[low_index] == word[high_index]:
        word = word[low_index + 1:high_index]
        if not word:
            return True

        return is_palindrome_recursive(word, low_index, len(word) - 1)

    return False
