def is_palindrome_iterative(word):
    """ Faça o código aqui. """
    new_word = []
    if len(word) == 0:
        return False
    for letter in list(word):
        new_word.insert(0, letter)
    if "".join(new_word) == word:
        return True
    else:
        return False
