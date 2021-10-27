def is_palindrome_iterative(word):
    if len(word) == 0:
        return False
    teste = word[::-1]
    return teste == word
