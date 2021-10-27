def is_palindrome_recursive(word, low_index, high_index):
    """ Faça o código aqui. """
    if not(word):
        return False
    if high_index - low_index <= 0:
        return True
    return (is_palindrome_recursive(word, low_index + 1, high_index - 1))

print(is_palindrome_recursive('socos', 0, 5))