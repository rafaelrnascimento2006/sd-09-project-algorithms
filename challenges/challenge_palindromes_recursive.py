def is_palindrome_recursive(word, low_index="", high_index=""):
    """Retorna True se for Palindromo e False se não for"""
    if _is_palindrome_recursive(word) == word:
        return True
    return False


def _is_palindrome_recursive(word):
    if word == "":
        return False

    if len(word) <= 1:
        return word

    return _is_palindrome_recursive(word[1:]) + word[0]


# print(is_palindrome_recursive(""))
# https://www.ti-enxame.com/pt/python/inverter-uma-string-sem-usar-reversed-ou-1/1042409120/
