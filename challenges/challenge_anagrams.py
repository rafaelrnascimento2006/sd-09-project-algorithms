from collections import Counter


def is_anagram(first_string, second_string):
    """ Faça o código aqui. """
    # https://codefather.tech/blog/anagrams-python/
    if len(first_string) != len(second_string):
        return False
    if(Counter(first_string) == Counter(second_string)):
        return True
    else:
        return False
