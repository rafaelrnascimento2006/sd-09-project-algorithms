def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    if not word:
        return False

    beginning, end = 0, len(word) - 1

    while end - beginning >= 1:
        if word[beginning] != word[end]:
            return False
        beginning += 1
        end -= 1

    return True
