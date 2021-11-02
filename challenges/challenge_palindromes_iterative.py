# Requisito 05
def is_palindrome_iterative(word):
    if not word:
        return False

    # [::-1] -> inverte a palavra
    if word != word[::-1]:
        return False

    return True
